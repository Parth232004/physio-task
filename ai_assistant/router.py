def classify_intent(user_input):
    """
    Classify the user's intent based on the input text.
    Returns one of: 'Q&A', 'Task request', 'Analysis request'
    """
    words = user_input.lower().split()

    # Keywords for Q&A
    qa_keywords = ['what', 'how', 'why', 'when', 'where', 'who', 'is', 'are', 'does']
    if any(keyword in words for keyword in qa_keywords) or '?' in user_input:
        return 'Q&A'

    # Keywords for Task request
    task_keywords = ['calculate', 'compute', 'do', 'execute', 'run', 'perform']
    if any(keyword in words for keyword in task_keywords):
        return 'Task request'

    # Keywords for Analysis request
    analysis_keywords = ['analyze', 'summarize', 'review', 'examine']
    if any(keyword in words for keyword in analysis_keywords):
        return 'Analysis request'

    # Default to Q&A if no match
    return 'Q&A'