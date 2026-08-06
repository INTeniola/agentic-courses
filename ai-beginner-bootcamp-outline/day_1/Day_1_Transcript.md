# Day 1 Video Transcript: Hire the Brain

[Open on instructor, medium shot, warm lighting]

Welcome to Day One of the Universal Knowledge Worker Bootcamp. I am genuinely glad you are here, because over the next five days you are going to build something that most people still believe is out of reach for beginners. You are going to build an AI agent that reads, reasons, researches, and reports, all on your behalf. And here is the honest truth I want you to hear before we touch a single line of code. You do not need a computer science degree for this. You need curiosity, and you need to show up for five days. That is the entry fee.

[Show slide 1: The Universal Knowledge Worker]

Let us talk about what we are actually building. Imagine hiring a research assistant. You hand them a messy question like, find out what my competitors are charging and summarise it into a one page brief. A good assistant does not ask you for step by step instructions. They go away, they search, they read, they think, they come back with an answer. That is what we are building. Not a chatbot that waits for you to spoon feed it. A worker.

[Show slide 2: Chatbot versus Agent]

So what is the difference between a chatbot and an agent? A chatbot is reactive. You speak, it replies, and the conversation ends there. It has a mouth, but no hands. An agent has both. An agent can decide to use a tool. It can search the web, open a file, call an API, run a calculation, and then look at what came back and decide what to do next. That single capability, the ability to take an action and learn from the result, is the entire revolution. Everything else we cover this week is just detail on top of that idea.

[Show slide 3: The Think, Act, Observe loop]

Which brings us to the most important concept of today. I want you to write these three words down, because we will return to them every single day. Think. Act. Observe.

Think is where the agent reasons about the goal. It looks at your instruction and asks itself, what do I actually need in order to answer this, and what should I do first?

Act is where the agent reaches into the world. It picks one tool and uses it. Maybe it runs a search. Maybe it reads a document you uploaded.

Observe is where the agent looks honestly at the result. Did that work? Did I get what I needed? If yes, it moves forward. If no, it adjusts and tries something else.

[Show slide 4: The loop animating in a circle]

And then it loops. Think, act, observe. Think, act, observe. Around and around until the goal is met. That is it. That is the machinery behind every impressive agent demonstration you have ever seen online. It is not magic. It is a loop with good judgement inside it.

Now, here is why today is called Hire the Brain. A loop is useless without something intelligent sitting at the centre making decisions. That intelligence is the model, and today we are going to hire ours. We will be using Google AI Studio and the Gemini family of models, because the free tier is genuinely generous, the setup takes minutes, and it is powerful enough to run everything we build this week.

[Switch to screen recording: Google AI Studio home page]

Follow along with me. Open your browser and go to Google AI Studio. Sign in with a standard Google account. You will land on a workspace that looks a little like a chat window with extra controls on the side. Do not be intimidated by the panels. We only care about three things today.

[Highlight the prompt area]

First, the prompt area. This is where we talk to the model. Let us type a simple instruction and watch it respond, just to confirm everything is alive.

[Highlight system instructions field]

Second, system instructions. This is where we tell the model who it is. This one field is how you turn a general model into a specialist. Type in something like, you are a careful research analyst who always cites sources.

[Highlight the Get API key button]

Third, and most importantly, find the button that says Get API key. Click it, create a key in a new project, and copy it somewhere private. Treat that key like your bank card PIN. Never post it in a screenshot, never paste it in a public chat.

[Cut back to instructor]

That key is your agent's employment contract. Guard it.

Your homework for today is short. Get your key working, and write one system instruction that defines the personality of your future assistant. Bring it to Day Two, because tomorrow we give this brain its hands. We start building tools.

Well done for starting. I will see you tomorrow.