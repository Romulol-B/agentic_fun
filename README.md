# agentic_fun

From LLM API calls to agent context aware and a specialized tool_set from the CLI.


0. Have a system prompt that reinforces the use of the toolset.
1. A toolset to list folders contents, read files and write .py .
2. After each call the LLM receive what action was called and the result.
3. The loop stops when there are no function calls or surpassing the max allowed calls
4. Folder write, read, and list location are injected on the code to increase security.


Functions folder has all the functions that the agent is allowed to call.


