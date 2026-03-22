
from prospectus_analysis_skill import ProspectusAnalysisSkill

skill = ProspectusAnalysisSkill()

text = "示例科技有限公司 招股书"
result = skill.run_from_text(text)

print(result)
