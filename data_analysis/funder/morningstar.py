import requests


def get_funds(n: int = 2**31-1, currency_country_code: str = "SWE") -> requests.Response:
    base_url = "https://tools.morningstar.se/api/rest.svc/klr5zyak8x/security/screener"
    params = {
        "page": 1,
        "pageSize": n,
        "sortOrder": "ReturnM12 DESC",
        "outputType": "json",
        "universeIds": f"FO{currency_country_code}$$ALL",
        "securityDataPoints": "SecId|Name|PriceCurrency|TenforeId|ReturnM0|ReturnM60|StandardDeviationM60|FundTNAV|StarRatingM255|Medalist_RatingNumber|SustainabilityRank|TrailingDate|ClosePrice|ReturnD1|ReturnW1|ReturnM1|ReturnM3|ReturnM6|ReturnM12|ReturnM36|ReturnM120|ReturnM180|MaxFrontEndLoad|MaximumExitCostAcquired|PerformanceFeeActual|FeeLevel|InitialPurchase|EquityStyleBox|BondStyleBox|AverageCreditQualityCode|EffectiveDuration|PortfolioDate|KID_SRI|MorningstarRiskM255|StandardDeviationM12|StandardDeviationM36|standardDeviationM120|Isin|ppmCode|TrackRecordExtension"
    }

    return requests.get(base_url, params)


def get_time_series(sec_id: str, currency: str = "SEK") -> requests.Response:
    base_url = "https://tools.morningstar.se/api/rest.svc/timeseries_price/n4omw1k3rh"
    params = {
        "id": sec_id,
        "currencyId": currency,
        "idtype": "morningstar",
        "frequenzy": "daily",
        "startDate": "0001-01-01",
        "endDate": "9999-12-31",
        "outputType": "COMPACTJSON"
    }

    return requests.get(base_url, params)
