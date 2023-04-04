# auto-coder: structured LLM colaboration

pick some file ending, `.llm_prompt` or something like that. ooooh better yet, combine that with a tag in the commit message, like `#4LLM`.  
tag triggers a github workflow which globs all the cached `.llm_prompt` files and sends them to the completion endpoint with a "flesh out this code" prompt.  
maybe you just want to have one function filled in. maybe you have a list of function names you want to have filled in.  
maybe you have just a docstring and you want to have the whole file filled in.

to be *really* generic, could add some kind of in-document template, like a yaml header that contains the prompt(s)/examples/whatever.

when the CI is triggered, a new document is generated for each `.llm_prompt`. same name, different file extension. default to `.py` or `.md`

for extra customization, this system could start by reading a config file. e.g. change the file extension targeted, default file extension to write, llm api, etc.
