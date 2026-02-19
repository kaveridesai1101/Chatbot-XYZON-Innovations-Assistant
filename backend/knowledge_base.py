from typing import Dict, List

KNOWLEDGE_BASE: Dict[str, Dict] = {
    "internship_query": {
        "apply": "Apply through our official Internship page by completing the online registration form. Focus on Tier 2 & 3 impact start right here!",
        "registration_loc": "Registration is exclusive to the official XYZON Innovations website's internship section.",
        "fee": "Registration details, including any applicable fees or scholarship options, are transparently mentioned in each program's description.",
        "account_required": "Yes, creating a student profile is necessary to track your progress and access the 3M+ learner community resources.",
        "requirements": "You'll need basic personal details, educational background, and contact information to begin your journey.",
        "confirmation": "Absolutely. A confirmation email is sent immediately upon successful registration to your provided address.",
        "wrong_email": "If you've entered the wrong email, please contact support@xyzon.in immediately to rectify your profile.",
        "edit_application": "For any edits after submission, please reach out to our support team for assistance.",
        "process": "The XYZON journey: Registration → Enrollment → LMS Access → Task Completion → Evaluation → Global Certification.",
        "start_date": "Program start dates are communicated via your enrollment confirmation and are synchronized with our global cohorts.",
        "tasks": "All industry-aligned tasks are assigned directly through your personalized LMS dashboard.",
        "tracking": "Real-time progress tracking is available 24/7 on your student dashboard.",
        "orientation": "Most programs begin with a virtual orientation to onboard you into our makerspace ecosystem.",
        "duration": "The internship duration is 3 months. During this period, interns work on real-world projects and gain practical experience in their selected domain.",
        "full_time_opportunity": "Yes ✅ After successfully completing the 3-month internship, high-performing interns may be eligible for a full-time opportunity, based on their performance and project evaluation.",
        "stipend": "Stipend details depend on performance and role selection. Interns selected for full-time opportunities may receive a stipend or compensation based on company policies.",
        "combined_logistics": "The internship duration is 3 months. After completion, interns who perform well may be considered for a full-time role. Selected candidates may receive a stipend based on performance and company policies.",
        "full_part_time": "We offer flexible tech internships that accommodate both full-time learners and part-time aspirants.",
        "payment_fee": "Transparency is key; all fee structures are clearly displayed on the respective internship landing pages.",
        "refund": "Detailed refund and cancellation policies are governed by our program terms, available on the portal.",
        "certificate": "Yes, industry-standard certificates are issued upon successful completion of all milestones.",
        "timing": "Certificates are typically generated within 7 business days after final evaluation.",
        "digital": "We issue verifiable digital certificates that can be shared globally on professional networks.",
        "download": "Yes, all your earned credentials remain available for download in your student dashboard.",
        "evaluation": "Performance is measured through continuous internal assignments and a final milestone project.",
        "final_assessment": "Yes, most tracks include a final evaluation to ensure global standard compliance.",
        "failure_policy": "Incomplete tasks may impact your certification eligibility. We provide mentor support to help you stay on track.",
        "remote": "Yes, to maximize reach in Tier 2 & 3 cities, the majority of our internships are 100% remote.",
        "wfh": "Our digital-first approach allows you to work comfortably from home while connecting to global projects.",
        "offline": "Most tech tracks are fully online, though some Makerspace events may have optional offline components.",
        "support": "Our dedicated support team is available via the contact form or email at support@xyzon.in.",
        "mentors": "Yes, we provide access to industry veterans who guide you through complex project tasks.",
        "available_domains": "We currently offer internships in the following domains:\n\n• MERN Stack Development\n• Generative AI\n• AI Project Development\n• Web Development\n• Full Stack Development\n\nPlease let me know which domain you are interested in.",
        "mern_details": "Yes, we offer a MERN Stack Internship.\n\nThis includes:\n• MongoDB\n• Express.js\n• React.js\n• Node.js\n• Real-world project development\n\nWould you like to know about duration, eligibility, or certification?",
        "gen_ai_details": "Yes, we offer a Generative AI Internship.\n\nThis program includes:\n• Prompt Engineering\n• AI Model Integration\n• Chatbot Development\n• AI-based Project Implementation\n\nWould you like details about duration or learning outcomes?",
        "ai_project_details": "Yes, we offer an AI Project Internship.\n\nThis includes:\n• Machine Learning basics\n• Model building\n• Real-world AI project development\n• Deployment concepts\n\nWould you like to know the eligibility criteria?",
        "web_dev_details": "Yes, we offer a Web Development Internship.\n\nThis covers:\n• HTML\n• CSS\n• JavaScript\n• Responsive Design\n• Frontend project building\n\nWould you like information about project structure or certification?",
        "full_stack_details": "Yes, we offer a Full Stack Development Internship.\n\nThis includes:\n• Frontend Development\n• Backend Development\n• Database Integration\n• Complete Web Application Projects\n\nWould you like to know about duration or enrollment process?",
        "best_domain_guidance": "The best domain depends on your interest:\n\n• Choose MERN Stack if you want modern web application development.\n• Choose Generative AI if you are interested in AI tools and chatbot systems.\n• Choose AI Project if you want machine learning exposure.\n• Choose Web Development if you want frontend specialization.\n• Choose Full Stack if you want complete end-to-end development skills.\n\nLet me know your interest, and I’ll guide you further."
    },
    "lms_support": {
        "login": "Access the XYZON LMS using your registered email and secure password at our portal.",
        "forgot_password": "Reset your access anytime using the 'Forgot Password' link; look for the recovery email in your inbox.",
        "login_issues": "If login fails, verify your credentials or clear your browser cache. Contact support if issues persist.",
        "lms_link": "The LMS login is prominently featured in our main website navigation for easy access.",
        "visibility": "Ensure your enrollment is confirmed. Courses typically sync to your dashboard within 24 hours.",
        "empty_dashboard": "This usually means your enrollment activation is pending. Please wait for the confirmation email.",
        "assignments": "Submit your tasks directly via the 'Assignments' module within your specific course area.",
        "edit_submission": "Submissions can be edited until the specified deadline, allowing for continuous refinement.",
        "file_formats": "We typically accept ZIP, PDF, and common codebase formats. Check the specific task brief.",
        "confirmation": "The LMS displays a 'Submitted' status and timestamp for every successful upload.",
        "tracking": "Track your learning journey phase-by-phase using the visual progress bar in the LMS.",
        "grades": "Live grades and feedback from evaluators are visible in the 'Grades' tab of your course.",
        "lesson_completion": "Lessons are automatically marked as complete once you've engaged with the full content.",
        "video_issues": "Refresh your browser or check your bandwidth. Our videos are optimized for even low-speed connections.",
        "pdf_issues": "Try downloading the file or using an alternative PDF viewer if it doesn't render in-browser.",
        "speed": "LMS performance is optimized; ensure your browser is up-to-date for the best experience.",
        "access_duration": "Your access lasts for the entirety of your enrollment period plus additional review time.",
        "extension": "Extensions are granted on a case-by-case basis depending on your program's specific policies.",
        "profile": "Update your photo, contact details, and bio through the 'Profile Settings' section.",
        "change_password": "For security, we recommend changing your password regularly via the 'Account Settings' tab.",
        "certificate_loc": "Once evaluation is positive, download your certificate directly from the 'Awards' section.",
        "support": "For urgent LMS issues, email lms-support@xyzon.in or use the internal helpdesk ticket system."
    },
    "resume_help": {
        "what_is": "The XYZON Resume Builder is a professional online tool designed to help you create high-impact, industry-standard resumes quickly using structured, ATS-friendly templates.",
        "access": "Access it directly from your Student Dashboard after logging into your official XYZON account.",
        "login_required": "Yes, login is absolutely mandatory to ensure your progress is saved and your data remains secure within your profile.",
        "is_free": "Access is currently open for all learners enrolled in our certified programs. Check your dashboard for your inclusive access status.",
        "how_to_create": "Simply select a professional template, enter your details in the guided sections, and use the preview mode before finalizing your PDF.",
        "templates": "We provide a curated set of templates optimized for tech, creative, and corporate roles to ensure you stand out.",
        "preview": "Yes, you can use the 'Live Preview' feature to see exactly how your resume looks before you decide to download it.",
        "required_details": "Focus on the core pillars: Personal Info, Education, Technical Skills, Projects, Experience, and your XYZON Certifications.",
        "edit_after_save": "Absolutely. You can log in anytime to update your profile, add new skills, or refine your project descriptions.",
        "change_template": "Yes, our builder allows you to switch between different professional layouts while keeping your entered content intact.",
        "update_skills": "Yes, your skills section is fully dynamic. We recommend updating it frequently as you complete more XYZON modules.",
        "delete_resume": "You can manage and delete your saved resumes directly from the Resume section of your dashboard.",
        "how_to_download": "Once satisfied, click the 'Download' button to generate your high-resolution PDF resume instantly.",
        "format": "For global compatibility and ATS performance, our resumes are exclusively generated in professional PDF format.",
        "download_issues": "If a download fails, refresh your page or check your internet stability. Clear your cache if the issue persists or contact support.",
        "multiple_downloads": "Yes, your saved resumes are available for unlimited downloads whenever you need them.",
        "skills_content": "Highlight technical tools, programming languages, and soft skills tailored specifically to the role you are targeting.",
        "project_desc": "Use the Google XYZON standard: explain the goal, the tech stack used, and your specific contribution or quantifiable impact.",
        "no_experience": "No problem! Focus on your academic projects, XYZON internships, specialized certifications, and core technical skills.",
        "certifications": "Yes, definitely include your XYZON Global Certifications (Oracle, Microsoft, etc.) to validate your skills to recruiters.",
        "data_saving": "If data isn't saving, ensure you have an active session. We recommend a stable connection for the best auto-save experience.",
        "page_load": "Try refreshing or switching to a modern browser like Chrome or Edge if the builder interface is slow to load.",
        "formatting": "If formatting looks off, double-check that you haven't used excessive special characters or empty line breaks in input fields.",
        "accidentally_deleted": "If you delete a section, you'll need to re-enter it. We recommend reviewing your content before confirming any deletions.",
        "length": "For students and interns, a concise, high-impact one-page resume is the industry gold standard.",
        "photo": "Include a professional photo only if it's a requirement for the specific creative role or region you are applying for.",
        "skills_count": "Quality over quantity. List 8-12 highly relevant skills matches the job description you're pursuing.",
        "customize": "Yes, every section is fully customizable to reflect your unique career journey and XYZON learning path.",
        "security": "Your data is protected by industry-standard encryption and is stored securely within the XYZON private infrastructure.",
        "visibility": "Your resume is private. Only you can view or download it unless you explicitly share your generated PDF.",
        "support": "Our technical support team is here to help! Reach out via the official contact form or email us at support@xyzon.in."
    },
    "course_query": {
        "what_courses": "XYZON offers Comprehensive Learning Solutions across Technical Certifications, Creative Skills Development, Faculty Development Programs (FDP), Software Product Engineering, Corporate Upskilling, and our flagship Makerspace Initiative.",
        "enrollment": "Explore and enroll through our official Courses page. Most programs are self-paced with flexible start dates, while some industry-aligned tracks follow structured cohort schedules.",
        "how_to_enroll": "Visit the specific course page, click 'Enroll Now,' complete your profile, and confirm your registration. You'll receive LMS access within 24 hours.",
        "account_required_enroll": "Yes, you need to create an account or log in before enrolling in any XYZON course.",
        "requirements": "Basic requirements vary by track. Technical courses may require foundational programming knowledge, while creative and FDP tracks are designed for all skill levels.",
        "beginner_courses": "Yes! We offer dedicated 'Beginner-to-Expert' tracks in Web Development, UI/UX Design, Digital Marketing, and Data Analytics specifically for absolute beginners.",
        "technical_certifications": "We provide industry-recognized certifications from Oracle, Microsoft, CompTIA, and other global leaders, ensuring your credentials are valued worldwide.",
        "creative_courses": "Our Creative Skills Development includes Animation, UI/UX Design, Graphic Design, Video Editing, and Digital Marketing—all project-based and portfolio-ready.",
        "fdp_programs": "Faculty Development Programs (FDP) are designed for educators to adopt modern pedagogy, integrate technology in teaching, and improve student placement outcomes by up to 300%.",
        "course_duration": "Course durations vary: Short-term certifications (4-8 weeks), Comprehensive programs (3-6 months), and FDP intensive workshops (1-2 weeks).",
        "self_paced": "Most courses are self-paced, allowing you to learn at your own speed and convenience. Industry-aligned tracks follow structured timelines to match real-world project cycles.",
        "live_classes": "Yes, select programs include live instructor-led sessions, Q&A forums, and mentor office hours for personalized guidance.",
        "assignments": "All courses include hands-on assignments, real-world projects, and evaluations to ensure you develop practical, job-ready skills.",
        "projects_included": "Yes, most tech courses include practical assignments and real-world projects to build your portfolio.",
        "quizzes_assessments": "Some courses include quizzes, assignments, or final assessments depending on the program structure.",
        "final_exam": "Certain courses may include a final evaluation to certify your mastery. Please refer to the specific course details page.",
        "certification_criteria": "To earn certification, you must complete all modules, submit required projects, and pass the final evaluation with a minimum score as specified in your program guidelines.",
        "certificate_validity": "XYZON certificates are lifetime credentials with verifiable digital signatures, recognized globally by employers and educational institutions.",
        "certificate_issuance": "Yes, a certificate is issued after successfully completing all required modules and assessments.",
        "certificate_timing": "Certificates are typically issued after completion verification, usually within 7 business days.",
        "certificate_download": "Certificates are available for download in your course dashboard once issued.",
        "course_fee": "Fee structures are transparently listed on each course page. We offer flexible payment options, early-bird discounts, and scholarship opportunities for deserving candidates.",
        "free_courses": "We periodically offer free introductory modules and webinars. Check our Courses page or subscribe to our newsletter for updates on free learning opportunities.",
        "refund_policy": "Refund policies vary by course. Please review the course-specific terms and conditions available on the enrollment page.",
        "prerequisites": "Prerequisites are clearly mentioned on each course page. Beginner tracks have no prerequisites, while advanced programs may require foundational skills or prior certifications.",
        "course_materials": "All course materials, including video lectures, PDFs, code repositories, and project templates, are accessible 24/7 through your LMS dashboard.",
        "content_types": "Courses typically include video lectures, reading materials, assignments, and hands-on project work.",
        "download_materials": "Download options depend on course settings. Please check inside your course dashboard for availability.",
        "mobile_access": "Yes, courses can generally be accessed through a mobile browser for learning on the go.",
        "instructor_access": "You can interact with instructors via live sessions, discussion forums, and dedicated Q&A modules within the LMS.",
        "mentor_support": "Some courses include mentor guidance. Please check the specific course details for mentor support availability.",
        "course_completion": "Track your completion status via the LMS progress bar. Courses are marked complete once all modules, assignments, and evaluations are successfully finished.",
        "track_progress": "You can track your progress in real-time through the course dashboard's visual progress indicators.",
        "see_scores": "If assessments are graded, your scores will be visible in your account under the Grades section.",
        "post_completion": "After completion, you retain access to course materials for revision, receive your certificate, and gain eligibility for advanced tracks and placement assistance.",
        "course_access_timing": "Course access is usually granted immediately after successful enrollment confirmation.",
        "course_not_visible": "Please ensure your enrollment is confirmed. If the issue continues, contact our support team at courses@xyzon.in.",
        "access_duration": "Access duration depends on the course enrollment period mentioned during registration. Check your course details for specific timelines.",
        "upgrade_course": "Yes, you can upgrade from a basic to a premium track or add specialized modules by contacting our enrollment team.",
        "multiple_courses": "Yes, you can enroll in multiple courses if it aligns with your learning goals and time availability.",
        "job_assistance": "Select programs include placement assistance, resume building, mock interviews, and access to our recruitment partner network.",
        "videos_not_loading": "Please refresh the page or check your internet connection. If the issue persists, contact our technical support team.",
        "page_not_opening": "Try clearing your browser cache or accessing the course from a different browser. Reach out to support if problems continue.",
        "support": "For course-related queries, reach out via the LMS helpdesk, email us at courses@xyzon.in, or use the contact form on our website."
    },
    "services_query": {
        "college_training": "Comprehensive curriculum design and delivery for educational institutions, including custom curriculum and faculty certification.",
        "corporate_training": "Tailored upskilling programs for organizations, featuring skill assessment and performance tracking.",
        "product_development": "End-to-end software development: MVP development, full-stack solutions, and technical consulting.",
        "makerspace": "Community-driven spaces connecting rural talent with global opportunities through mentorship and freelance marketplaces.",
        "hackathons": "Immersive hackathon-led learning modules for rapid skill acquisition and innovation.",
        "entrepreneurship": "Support framework for student & rural founders to ideate, validate and scale ventures."
    },
    "success_stories": {
        "stories": [
            "Priya Sharma (Software Developer @ TCS): Small town to Global Career.",
            "Ramesh Kumar (Freelance Developer): Farming to Freelancing, earning 50K+ monthly.",
            "Dr. Ananya Patel (Professor): Revolutionized teaching methodology, improving placements by 300%.",
            "Suresh Patel (Technical Lead @ Infosys): Zero knowledge to leading a team of 15.",
            "Meera Reddy (Startup Founder): Built MVP through Xyzon's program and got seed funding."
        ]
    },
    "website_help": {
        "navigation": "You can explore our main sections via the navigation menu: 'Home', 'Programs', 'Internships', 'Courses', 'Services', 'Success Stories', and 'Contact Us'.",
        "find_internships": "Visit the 'Internships' page in the main navigation menu to explore all available internship opportunities.",
        "find_courses": "Click on 'Courses' in the navigation menu to browse our comprehensive learning solutions across Technical, Creative, and FDP tracks.",
        "about_xyzon": "Learn about our mission, vision, and impact on the 'About Us' section, accessible from the homepage or footer.",
        "services_page": "Navigate to 'Services' to explore our College Training, Corporate Upskilling, Product Development, Makerspace, and Entrepreneurship support offerings.",
        "success_stories": "Visit the 'Success Stories' section to read inspiring journeys of our 3M+ learners who've transformed their careers through XYZON.",
        "homepage": "Click on the XYZON logo in the top-left corner of any page to return to the homepage.",
        "footer_navigation": "Our footer contains a complete sitemap with links to all major sections, policies, and contact information.",
        "search_function": "Use the search bar (if available) or navigate through our organized menu sections to find specific programs or information.",
        "mobile_navigation": "On mobile devices, tap the menu icon (hamburger) in the top-right corner to access the full navigation menu.",
        "contact_email": "Reach out to us at contact@xyzon.in for general inquiries, or use specialized emails: support@xyzon.in (technical), courses@xyzon.in (courses), lms-support@xyzon.in (LMS issues).",
        "contact_phone": "Call us at +91 87542 00247 during business hours for immediate assistance.",
        "contact_form": "Use the 'Contact Us' page to submit a detailed inquiry through our web form. We respond within 24-48 hours.",
        "office_location": "Visit us at: CAMPUS 1A, NO.143, DR.M.G.R. ROAD, Perungudi, Chennai - 600096, Tamil Nadu, India.",
        "business_hours": "We're available Monday - Friday: 9:00 AM - 6:00 PM IST. For urgent technical issues, use our 24/7 email support.",
        "emergency_support": "For critical technical issues outside business hours, email support@xyzon.in with 'URGENT' in the subject line.",
        "social_media": "Connect with us on our social media channels (links available in the footer) to stay updated on programs, success stories, and opportunities.",
        "newsletter": "Subscribe to our newsletter via the homepage signup form to receive updates on new courses, free webinars, and scholarship opportunities.",
        "chat_support": "You're currently using our AI chatbot! For human assistance, please use the contact form or email us directly.",
        "feedback": "We value your feedback! Share your experience via the contact form or email us at feedback@xyzon.in.",
        "technical_issues": "For website technical issues (page errors, login problems), email support@xyzon.in with details and screenshots if possible.",
        "partnership_inquiry": "For corporate partnerships, college collaborations, or B2B inquiries, email us at partnerships@xyzon.in with your proposal.",
        "media_inquiry": "Media and press inquiries can be directed to media@xyzon.in.",
        "careers": "Interested in joining the XYZON team? Check our 'Careers' page (if available) or email careers@xyzon.in with your resume.",
        "privacy_policy": "Our Privacy Policy is accessible via the footer link, detailing how we protect and use your data.",
        "terms_of_service": "Terms of Service governing platform usage are available in the footer section.",
        "accessibility": "We're committed to accessibility. If you encounter any accessibility issues, please contact support@xyzon.in."
    },
    "greeting": {
        "message": "Hello 👋\nI'm the AI Assistant for XYZON.\nHow can I help you today?\n\nYou can ask about:\n• Internships\n• Courses\n• LMS Support\n• Resume Builder\n• Website Guidance"
    },
    "acknowledgment": {
        "message": "Thank you 😊\nHow may I assist you further?\n\nWould you like help with:\n• Internship information\n• Course enrollment\n• LMS access\n• Resume building guidance"
    },
    "thanks": {
        "message": "You're welcome 😊\nIf you need any more assistance, feel free to ask."
    },
    "goodbye": {
        "message": "Thank you for visiting XYZON.\nHave a great day ahead! 👋"
    },
    "help_request": {
        "message": "I'm here to help 😊\n\nPlease tell me which area you need assistance with:\n\n• Internship\n• Courses\n• LMS\n• Resume Builder"
    },
    "unsure": {
        "message": "I can assist you with:\n\n• Internship details and process\n• Course information\n• LMS support\n• ATS-friendly resume guidance\n• Website navigation\n\nPlease let me know what you need help with."
    },
    "random_text": {
        "message": "I'm sorry, I didn't understand that.\nYou can ask me about internships, courses, LMS support, or resume guidance."
    },
    "repeat_okay": {
        "message": "No problem 😊\nPlease let me know your question, and I'll be happy to assist you."
    },
    "fallback": {
        "message": "I'm sorry, as your XYZON AI Assistant, I can help with information about our programs (3M+ learners served), services, and internship processes. If you'd like to reach out directly, please use our contact form or email us at contact@xyzon.in."
    },
    "welcome": {
        "message": "Hello 👋 Welcome to XYZON Innovations!\n\"Transforming India into the Global Development Hub.\"\nHow can I help you explore our world-class certifications, Makerspace initiatives, or corporate services today?"
    },
    "escalation": {
        "message": "For personalized assistance, stay in touch with our team at contact@xyzon.in or visit us at our Chennai campus."
    }
}



