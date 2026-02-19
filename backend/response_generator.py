import re
from typing import List, Tuple

class IntentClassifier:
    def __init__(self):
        # Conversational intents (checked first for natural flow)
        self.conversational_intents = {
            "greeting": [r"\b(hi|hello|hey|good\s+(morning|afternoon|evening)|greetings)\b"],
            "thanks": [r"\b(thank(s| you)|thx|appreciate)\b"],
            "goodbye": [r"\b(bye|goodbye|see\s+you|take\s+care|have\s+a\s+good\s+day)\b"],
            "acknowledgment": [r"^\b(ok|okay|fine|alright|sure|yeah|yep|yes)\b$"],
            "help_request": [r"\b(help\s+me|i\s+need\s+help|assist\s+me|can\s+you\s+help)\b"],
            "unsure": [r"\b(i\s+don'?t\s+know|not\s+sure|what\s+can\s+you\s+do|unsure)\b"],
        }
        
        # Domain-specific intents (checked after conversational intents)
        self.domain_intents = {
            "internship_domains": [r"which\s+internship\s+domains", r"what\s+internships\s+do\s+you\s+offer", r"available\s+internship\s+fields"],
            "mern_internship": [r"mern\s+internship", r"do\s+you\s+offer\s+mern", r"mongodb\s+react\s+internship"],
            "gen_ai_internship": [r"gen\s+ai\s+internship", r"generative\s+ai\s+program", r"chatgpt\s+project\s+internship"],
            "ai_project_internship": [r"ai\s+project\s+internship", r"artificial\s+intelligence\s+internship"],
            "web_dev_internship": [r"web\s+developer\s+internship", r"frontend\s+internship"],
            "full_stack_internship": [r"full\s+stack\s+internship", r"backend\s+\+\s+frontend\s+internship"],
            "best_domain": [r"which\s+domain\s+is\s+best"],
            "internship_duration": [r"duration\s+of\s+internship", r"how\s+long\s+is\s+the\s+internship", r"internship\s+period"],
            "full_time_opportunity": [r"full-time\s+opportunity", r"job\s+after\s+internship", r"hired\s+after\s+internship"],
            "stipend_query": [r"internship\s+paid", r"provide\s+stipend", r"is\s+there\s+salary", r"stipend"],
            "internship_query": [r"internship", r"intern", r"process", r"duration", r"certificate"],
            "lms_support": [r"lms", r"login", r"password", r"visible", r"access"],
            "resume_help": [r"resume", r"template", r"pdf", r"builder"],
            "course_query": [r"course", r"enroll", r"self-paced", r"project"],
            "website_help": [r"navigation", r"contact", r"support", r"menu", r"how\s+to", r"find"]
        }

    def classify(self, query: str) -> str:
        query_lower = query.lower().strip()
        
        # Check for combined logistics first for smart handling
        if re.search(r"duration", query_lower) and (re.search(r"stipend", query_lower) or re.search(r"paid", query_lower) or re.search(r"salary", query_lower)):
            return "combined_logistics"
        
        # Check for conversational intents first
        for intent, patterns in self.conversational_intents.items():
            for pattern in patterns:
                if re.search(pattern, query_lower):
                    return intent
        
        # Check for domain-specific intents
        for intent, patterns in self.domain_intents.items():
            for pattern in patterns:
                if re.search(pattern, query_lower):
                    return intent
        
        # Check for random/gibberish text (no letters or very short)
        if len(query_lower) < 2 or not re.search(r'[a-z]', query_lower):
            return "random_text"
        
        # Default fallback
        return "fallback"

class ResponseGenerator:
    def __init__(self, knowledge_base: dict):
        self.kb = knowledge_base

    def generate_response(self, intent: str, query: str, context: List[dict]) -> str:
        # Handle conversational intents first
        if intent in ["greeting", "thanks", "goodbye", "help_request", "unsure", "acknowledgment", "random_text"]:
            return self.kb[intent]["message"]
        
        # Handle domain-specific internship queries
        if intent == "internship_domains":
            return self.kb["internship_query"]["available_domains"]
        elif intent == "mern_internship":
            return self.kb["internship_query"]["mern_details"]
        elif intent == "gen_ai_internship":
            return self.kb["internship_query"]["gen_ai_details"]
        elif intent == "ai_project_internship":
            return self.kb["internship_query"]["ai_project_details"]
        elif intent == "web_dev_internship":
            return self.kb["internship_query"]["web_dev_details"]
        elif intent == "full_stack_internship":
            return self.kb["internship_query"]["full_stack_details"]
        elif intent == "best_domain":
            return self.kb["internship_query"]["best_domain_guidance"]
        elif intent == "internship_duration":
            return self.kb["internship_query"]["duration"]
        elif intent == "full_time_opportunity":
            return self.kb["internship_query"]["full_time_opportunity"]
        elif intent == "stipend_query":
            return self.kb["internship_query"]["stipend"]
        elif intent == "combined_logistics":
            return self.kb["internship_query"]["combined_logistics"]
        
        # Escalation logic: If user repeats same unclear question twice
        if intent == "fallback" and len(context) >= 2:
            last_msgs = [m["content"].lower() for m in context if m["role"] == "user"]
            if len(last_msgs) >= 2 and last_msgs[-1] == query.lower():
                return self.kb["escalation"]["message"]

        if intent == "fallback":
            return self.kb["fallback"]["message"]

        data = self.kb.get(intent, {})
        
        if intent == "internship_query":
            process = data.get('process', 'Registration → Enrollment → LMS Access')
            duration = data.get('duration', '3 months')
            certificate = data.get('certificate', 'Issued upon completion')
            return f"Our internship process is: {process} It typically lasts {duration}. Certificates are {certificate.lower()}."
        
        elif intent == "lms_support":
            if "password" in query.lower():
                return f"To reset your password, {data.get('forgot_password', 'use the Forgot Password link on the portal.')}"
            elif "visible" in query.lower() or "find" in query.lower():
                return data.get('visibility', data.get('course_not_visible', 'Please ensure your enrollment is confirmed.'))
            else:
                login_info = data.get('login', 'Access the portal using your registered email.')
                visibility_info = data.get('visibility', data.get('course_not_visible', 'Wait 24 hours for courses to sync.'))
                return f"{login_info} {visibility_info}"

        elif intent == "resume_help":
            what_is = data.get('what_is', 'Our Resume Builder helps you create ATS-friendly resumes.')
            how_to = data.get('how_to_create', 'Select a template and enter your details in your dashboard.')
            return f"{what_is} {how_to}"

        elif intent == "course_query":
            what_courses = data.get('what_courses', 'We offer various technical and creative courses.')
            enrollment = data.get('enrollment', 'Enroll through our official Courses page.')
            return f"{what_courses} {enrollment}"

        elif intent == "website_help":
            navigation = data.get('navigation', 'Use the main menu to navigate.')
            contact = data.get('contact_email', data.get('contact', 'Email us at support@xyzon.in'))
            return f"{navigation} For further help, contact {contact.lower()}"

        return self.kb.get("fallback", {}).get("message", "I'm sorry, I couldn't process that.")
