def enrich_event(ip, score):
    intel = check_ip(ip)

    abuse_score = intel["data"]["abuseConfidenceScore"]

    if abuse_score > 80:
        score += 30

    return {
        "ip": ip,
        "risk_score": score,
        "threat_score": abuse_score
    }
