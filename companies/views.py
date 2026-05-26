import pandas as pd

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Company, RawRecord, ESGResult
from .esg import calculate_esg_score


# -------------------------
# COMPANY LIST
# -------------------------
@api_view(['GET'])
def company_list(request):
    companies = Company.objects.all().values()
    return Response(companies)


# -------------------------
# CSV UPLOAD + ESG CALCULATION
# -------------------------
@api_view(['POST'])
def upload_csv(request):

    company_id = request.data.get("company")
    file = request.FILES.get("csv_file")

    if not company_id or not file:
        return Response(
            {"error": "company and csv_file required"},
            status=400
        )

    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist:
        return Response(
            {"error": "Company not found"},
            status=404
        )

    # Save raw file
    raw = RawRecord.objects.create(
        company=company,
        csv_file=file
    )

    # Read CSV
    df = pd.read_csv(raw.csv_file.path)
    df.columns = df.columns.str.strip()

    # ---------------- ESG LOGIC ----------------
    if "Fuel_Liters" in df.columns:
        travel_df = df
        utility_df = pd.DataFrame(columns=["KWH"])
        result = calculate_esg_score(travel_df, utility_df)

    elif "KWH" in df.columns:
        utility_df = df
        travel_df = pd.DataFrame(columns=["Fuel_Liters"])
        result = calculate_esg_score(travel_df, utility_df)

    elif "Distance_KM" in df.columns:
        df["emissions"] = df["Distance_KM"].abs() * 0.15

        result = {
            "total_flight_km": df["Distance_KM"].abs().sum(),
            "flight_emissions": df["emissions"].sum(),
            "message": "Flight ESG data processed successfully"
        }

    else:
        result = {
            "message": "Unknown CSV format",
            "available_columns": list(df.columns)
        }

    # ---------------- SAVE TO DATABASE ----------------
    ESGResult.objects.create(
        company=company,
        total_fuel=result.get("total_fuel", 0),
        total_kwh=result.get("total_kwh", 0),
        flight_km=result.get("total_flight_km", 0),
        co2_emissions=result.get("co2_emissions", 0),
        esg_score=result.get("esg_score", 0),
    )

    return Response({
        "message": "CSV Uploaded Successfully",
        "rows": len(df),
        "esg": result
    })


# -------------------------
# ESG HISTORY API
# -------------------------
@api_view(['GET'])
def esg_history(request, company_id):
    data = ESGResult.objects.filter(company_id=company_id).values()
    return Response(data)