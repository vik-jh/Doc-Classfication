import re

def extract_entities(document_text, doc_type):
    # Customize extraction based on doc_type
    if doc_type == "Car Insurance":
        insurer_name = re.search(r"Insurer Name:\s*(.*)", document_text)
        car_details = re.search(r"Car:\s*(.*)", document_text)
        premium = re.search(r"Premium:\s*\$([0-9,]+)", document_text)
        start_date = re.search(r"Start Date:\*(.*)", document_text)
        end_date = re.search(r"End Date:\*(.*)", document_text)
        # Add more fields as needed
        return {
            "insurer_name": insurer_name.group(1) if insurer_name else None,
            "car_details": car_details.group(1) if car_details else None,
            "premium": premium.group(1) if premium else None,
            "start_date" : start_date.group(1)if start_date else None,
            "end_date" : end_date.group(1) if end_date else None,
        }
    elif doc_type == "Home Insurance":
        # Add extraction logic for home insurance
        insurer_name = re.search(r"Insurer Name:\s*(.*)", document_text)
        home_Details = re.search(r"home:\s*(.*)", document_text)
        premium = re.search(r"Premium:\s*\$([0-9,]+)",document_text)
        start_date =re.search(r"Start Date:\s*(.*)", document_text)
        end_date = re.search(r"End Date:\*(.*)", document_text)
        return{
            "insurer_name": insurer_name.group(1) if insurer_name else None,
            "home_Details": home_Details.group(1) if home_Details else None,
            "premium": premium.group(1) if premium else None,
            "start_date" : start_date.group(1)if start_date else None,
            "end_date" : end_date.group(1) if end_date else None,
        }
    elif doc_type == "Health Insurance":
        # Add extraction logic for health insurance
        insurer_name = re.search(r"Insurer Name:\s*(.*)", document_text)
        health_Details = re.search(r"health:\s*(.*)", document_text)
        premium = re.search(r"Premium:\s*\$([0-9,]+)",document_text)
        start_date =re.search(r"Start Date:\s*(.*)", document_text)
        end_date = re.search(r"End Date:\*(.*)", document_text)
        
        return{
            "insurer_name": insurer_name.group(1) if insurer_name else None,
            "health_Details": health_Details.group(1) if health_Details else None,
            "premium": premium.group(1) if premium else None,
            "start_date" : start_date.group(1)if start_date else None,
            "end_date" : end_date.group(1) if end_date else None,
        }
        
        pass
    return {}
