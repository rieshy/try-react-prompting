# ReAct Prompting Example

This project demonstrates ReAct (Reasoning + Acting) prompting using LangChain, which combines reasoning and action in an iterative process to solve complex tasks.

## Setup

1. Create a `.env` file in the root directory with your API keys:
```
SERPAPI_API_KEY=your_serpapi_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

3. Run the example:
```
python main.py
```

## What is ReAct Prompting?

ReAct is a prompting technique that combines:
- **Reasoning**: Having the LLM think through a problem step by step
- **Acting**: Having the LLM use tools to gather information

The format follows this pattern:
1. **Thought**: Reasoning about what to do next
2. **Action**: Choosing a tool to use
3. **Action Input**: Providing input to the tool
4. **Observation**: Getting the result from the tool
5. Repeating until reaching a final answer

This approach helps LLMs break down complex tasks, gather relevant information, and avoid hallucination by grounding responses in real data.

