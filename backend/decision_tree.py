def evaluate_compliance(response_data):
    score = 0
    issues = []
    compliance = []

    checks = [
        ("has_dpo", "Encarregado de dados nomeado"),
        ("legal_basis", "Base legal mencionada"),
        ("uses_sensitive_data", "Tratamento de dados sensíveis"),
        ("security_measures", "Medidas de segurança aplicadas"),
        ("has_consent_process", "Processo de consentimento claro"),
        ("data_encrypted", "Criptografia aplicada"),
        ("has_retention_policy", "Política de retenção existente"),
        ("rights_accessible", "Direitos dos titulares acessíveis"),
        ("shared_with_consent", "Compartilhamento com consentimento"),
        ("has_privacy_assessment", "Avaliação de impacto realizada")
    ]

    for key, description in checks:
        if response_data.get(key):
            score += 10
            compliance.append(description)
        else:
            issues.append(f"{description} não atendido")

    return {
        "score": score,
        "level": "Alto" if score >= 70 else "Médio" if score >= 40 else "Baixo",
        "issues": issues,
        "compliance": compliance
    }
