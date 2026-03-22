
class ProspectusAnalysisSkill:
    def run_from_text(self, text: str):
        return {
            "schema_version": "1.0",
            "structured_fields": {
                "company_name": {
                    "raw": text[:20],
                    "normalized": text[:20],
                    "confidence": 0.5
                }
            },
            "semantic_fields": {},
            "extraction_meta": {}
        }
