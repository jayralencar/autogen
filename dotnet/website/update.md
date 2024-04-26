##### Update on 0.0.12 (2024-04-22)
- Add AutoGen.Mistral package to support Mistral.AI models

##### Update on 0.0.11 (2024-04-10)
- Add link to Discord channel in nuget's readme.md
- Document improvements
- In `AutoGen.OpenAI`, update `Azure.AI.OpenAI` to 1.0.0-beta.15 and add support for json mode and deterministic output in `OpenAIChatAgent` [Issue #2346](https://github.com/microsoft/autogen/issues/2346)
- In `AutoGen.SemanticKernel`, update `SemanticKernel` package to 1.7.1
- [API Breaking Change] Rename `PrintMessageMiddlewareExtension.RegisterPrintFormatMessageHook' to `PrintMessageMiddlewareExtension.RegisterPrintMessage`.
##### Update on 0.0.10 (2024-03-12)
- Rename `Workflow` to `Graph`
- Rename `AddInitializeMessage` to `SendIntroduction`
- Rename `SequentialGroupChat` to `RoundRobinGroupChat`
##### Update on 0.0.9 (2024-03-02)
- Refactor over @AutoGen.Message and introducing `TextMessage`, `ImageMessage`, `MultiModalMessage` and so on. PR [#1676](https://github.com/microsoft/autogen/pull/1676)
- Add `AutoGen.SemanticKernel` to support seamless integration with Semantic Kernel
- Move the agent contract abstraction to `AutoGen.Core` package. The `AutoGen.Core` package provides the abstraction for message type, agent and group chat and doesn't contain dependencies over `Azure.AI.OpenAI` or `Semantic Kernel`. This is useful when you want to leverage AutoGen's abstraction only and want to avoid introducing any other dependencies.
- Move `GPTAgent`, `OpenAIChatAgent` and all openai-dependencies to `AutoGen.OpenAI`
##### Update on 0.0.8 (2024-02-28)
- Fix [#1804](https://github.com/microsoft/autogen/pull/1804)
- Streaming support for IAgent [#1656](https://github.com/microsoft/autogen/pull/1656)
- Streaming support for middleware via `MiddlewareStreamingAgent` [#1656](https://github.com/microsoft/autogen/pull/1656)
- Graph chat support with conditional transition workflow [#1761](https://github.com/microsoft/autogen/pull/1761)
- AutoGen.SourceGenerator: Generate `FunctionContract` from `FunctionAttribute` [#1736](https://github.com/microsoft/autogen/pull/1736)
##### Update on 0.0.7 (2024-02-11)
- Add `AutoGen.LMStudio` to support comsume openai-like API from LMStudio local server
##### Update on 0.0.6 (2024-01-23)
- Add `MiddlewareAgent`
- Use `MiddlewareAgent` to implement existing agent hooks (RegisterPreProcess, RegisterPostProcess, RegisterReply)
- Remove `AutoReplyAgent`, `PreProcessAgent`, `PostProcessAgent` because they are replaced by `MiddlewareAgent`
##### Update on 0.0.5
- Simplify `IAgent` interface by removing `ChatLLM` Property
- Add `GenerateReplyOptions` to `IAgent.GenerateReplyAsync` which allows user to specify or override the options when generating reply

##### Update on 0.0.4
- Move out dependency of Semantic Kernel
- Add type `IChatLLM` as connector to LLM

##### Update on 0.0.3
- In AutoGen.SourceGenerator, rename FunctionAttribution to FunctionAttribute
- In AutoGen, refactor over ConversationAgent, UserProxyAgent, and AssistantAgent

##### Update on 0.0.2
- update Azure.OpenAI.AI to 1.0.0-beta.12
- update Semantic kernel to 1.0.1