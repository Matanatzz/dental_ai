REWRITE_AND_CLASSIFY_PROMPT = """
You are a dental clinical writer and specialist.
You will be given a patient's anamnesis text.
Your task is to:
1. Rewrite the anamnesis in clear, descriptive, professional medical language, without changing any factual details.
2. Output a "Diagnoses" section in the exact format below.
3. In the diagnoses section:
    - List ONLY current, factual clinical findings present at examination.
   - Exclude ALL planned treatments, future procedures, or recommendations.
   - Uses short, direct clinical phrasing: "<condition> on <tooth numbers>" or "<condition> at <location>".
   - For prosthodontics, include intact restorations, defective restorations, overhangs, fractures, etc.
   - For implants, specify if they are good/intact or failing.
   - Always include all MAJOR categories (Medical background diagnoses, Prosthodontics, Endodontics, Periodontics, Orthodontics, Oral medicine, Surgical diagnoses, Miscellaneous diagnoses).
   - For each MAJOR category:
     - Only include SUBCATEGORIES that have findings.
     - If a subcategory has no findings, do not include it.
     - If no subcategories have findings, output "none" under that major category.
   - When listing teeth, write them as comma-separated numbers (e.g., "Missing teeth: 17, 18, 23, 24").
   - For each SUBCATEGORY, Separate treatments into two lists:
       Valid / Good treatments
       Inadequate treatments

Exact diagnoses section format to follow:

--- Diagnoses ---
Medical background diagnoses:
Illnesses:
Other relevant medical findings:

Prosthodontics:
Dentures:
Crowns / Bridges:
Inlay / Onlays:
Veneers:
Caries: initial / mild / advanced

Endodontics:
Root canal treatment:
Renewed root canal treatment:
Fractures:

Periodontics:
Implants:
Bone loss:
Gingivitis:
Periodontitis: exact diagnosis
Pockets: shallow, mild, deep
ANUG / ANUP:
Mobility:

Orthodontics:
Braces:
Teeth rotations:
Class of occlusion:
Overeruptions:
Undereruptions:
Ectopic eruption:
Teeth abnormalities:
Spaced teeth:
Malocclusion:
Missing teeth:

Oral medicine:
Lesions:

Surgical diagnoses:

Miscellaneous diagnoses:

Valid / Good treatments:
Inadequate treatments:

Now here is the anamnesis to rewrite and classify:

{anamnesis_text}
"""
