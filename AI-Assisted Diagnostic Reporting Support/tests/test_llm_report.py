from backend.ai_engine.llm_report import generate_report

def test_report_generation():
    report = generate_report("Test findings")
    assert "Technique:" in report
    assert "Findings: Test findings" in report
    assert "Impression:" in report