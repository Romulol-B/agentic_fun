# agentic_fun

From LLM API calls to agent context aware and a specialized tool_set from the CLI.


0. Have a system prompt that reinforces the use of the toolset.
1. A toolset to list folders contents, read files and write .py .
2. After each call the LLM receive what action was called and the result.
3. The loop stops when there are no function calls or surpassing the max allowed calls
4. Folder write, read, and list location are injected on the code to increase security.


Functions folder has all the functions that the agent is allowed to call.

## Motivation.

My intention is this project to grow and be the agent that perform from the action list and be less prone to hallucination.

### Quick start:
Remember before any prompt you need setup your API keys on a .env file.

```bash
git clone https://github.com/Romulol-B/agentic_fun
uv .venv venv
source .venv/bin/activate
uv main.py [-h] [--verbose] user_prompt
```
- positional arguments:
    - user_prompt User prompt
- options:
    - -h, --help show a help message and exit.
    - --verbose  Enable verbose output.
<img width="700" height="300" alt="terminal" src="https://github.com/user-attachments/assets/b6cd95c5-3fcb-45e4-bc20-a61875f60ec2" />


