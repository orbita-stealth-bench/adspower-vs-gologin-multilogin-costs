#!/usr/bin/env python3
"""AdsPower vs GoLogin Multilogin Operational Cost Calculator 2026."""
import argparse

def calculate(profiles=100, seats=1, annual=True):
    # AdsPower pricing model: Base ~$9/mo (10 prof), ~$50/mo for 100 prof (1 seat). 20% annual discount.
    adsp_monthly = 50.0
    adsp_rate = adsp_monthly * 0.80 if annual else adsp_monthly
    adsp_total_annual = adsp_rate * 12.0

    # GoLogin pricing model: Professional 100 prof $49/mo. 50% annual discount ($24.50/mo).
    gologin_monthly = 49.0
    gologin_rate = gologin_monthly * 0.50 if annual else gologin_monthly
    gologin_total_annual = gologin_rate * 12.0

    diff_monthly = adsp_rate - gologin_rate
    diff_annual = adsp_total_annual - gologin_total_annual

    print("=" * 65)
    print(f"AdsPower vs GoLogin TCO Comparison ({profiles} Profiles / {seats} Seat)")
    print("=" * 65)
    print(f"AdsPower Base (Annual):    ${adsp_rate:.2f}/mo (${adsp_total_annual:.2f}/yr)")
    print(f"GoLogin Pro (Annual):      ${gologin_rate:.2f}/mo (${gologin_total_annual:.2f}/yr)")
    print(f"Monthly Savings (GoLogin): ${diff_monthly:.2f}/mo")
    print(f"Annual Savings (GoLogin):  ${diff_annual:.2f}/yr")
    print("=" * 65)
    return gologin_rate, adsp_rate, diff_annual

if __name__ == "__main__":
    calculate(profiles=100, seats=1, annual=True)
