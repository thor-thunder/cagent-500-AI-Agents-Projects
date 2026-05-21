# AI Agents Documentation

[![500-AI-Agents-Projects](https://img.shields.io/badge/500--AI--Agents--Projects-Catalog-2ea44f?logo=github)](https://github.com/ashishpatel26/500-AI-Agents-Projects)

Comprehensive documentation of all AI agent use cases cataloged in this repository. Covers ~134 agents across 5 categories: industry use cases and 4 major frameworks (CrewAI, AutoGen, Agno, LangGraph).

Upstream source: [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) — 30,000+ stars, validated active.

---

## Quick Stats

| Metric | Value |
|--------|-------|
| Total agent use cases | ~134 |
| Frameworks covered | 4 (CrewAI, AutoGen, Agno, LangGraph) |
| Industries covered | 15+ |
| Industry use cases | 22 |
| CrewAI agents | 22 |
| AutoGen agents | ~50 |
| Agno agents | 18 |
| LangGraph agents | 22 |

---

## Table of Contents

- [Master Index](#master-index)
- [Industry Use Cases](#1-industry-use-cases)
- [CrewAI Agents](#2-crewai-agents)
- [AutoGen Agents](#3-autogen-agents)
- [Agno Agents](#4-agno-agents)
- [LangGraph Agents](#5-langgraph-agents)
- [Contributing](#contributing)

---

## Master Index

Flat searchable reference of all agents. Links in per-section tables below.

| # | Agent Name | Framework | Industry | Description |
|---|-----------|-----------|----------|-------------|
| 1 | HIA (Health Insights Agent) | Industry | Healthcare | Analyses medical reports and provide health insights |
| 2 | AI Health Assistant | Industry | Healthcare | Diagnoses and monitors diseases using patient data |
| 3 | Automated Trading Bot | Industry | Finance | Automates stock trading with real-time market analysis |
| 4 | Virtual AI Tutor | Industry | Education | Provides personalized education tailored to users |
| 5 | 24/7 AI Chatbot | Industry | Customer Service | Handles customer queries around the clock |
| 6 | Product Recommendation Agent | Industry | Retail | Suggests products based on user preferences and history |
| 7 | Self-Driving Delivery Agent | Industry | Transportation | Optimizes routes and autonomously delivers packages |
| 8 | Factory Process Monitoring Agent | Industry | Manufacturing | Monitors production lines and ensures quality control |
| 9 | Property Pricing Agent | Industry | Real Estate | Analyzes market trends to determine property prices |
| 10 | Smart Farming Assistant | Industry | Agriculture | Provides insights on crop health and yield predictions |
| 11 | Energy Demand Forecasting Agent | Industry | Energy | Predicts energy usage to optimize grid management |
| 12 | Content Personalization Agent | Industry | Entertainment | Recommends personalized media based on preferences |
| 13 | Legal Document Review Assistant | Industry | Legal | Automates document review and highlights key clauses |
| 14 | Recruitment Recommendation Agent | Industry | Human Resources | Suggests best-fit candidates for job openings |
| 15 | Virtual Travel Assistant | Industry | Hospitality | Plans travel itineraries based on preferences |
| 16 | AI Game Companion Agent | Industry | Gaming | Enhances player experience with real-time assistance |
| 17 | Real-Time Threat Detection Agent | Industry | Cybersecurity | Identifies potential threats and mitigates attacks |
| 18 | E-commerce Personal Shopper Agent | Industry | E-commerce | Helps customers find products they'll love |
| 19 | Logistics Optimization Agent | Industry | Supply Chain | Plans efficient delivery routes and manages inventory |
| 20 | Vibe Hacking Agent | Industry | Cybersecurity | Autonomous multi-agent based red team testing service |
| 21 | MediSuite-Ai-Agent | Industry | Health Insurance | Automates hospital/insurance claiming workflow |
| 22 | Lina-Egyptian-Medical-Chatbot | Industry | Health Insurance | AI medical chatbot for hospital/insurance workflow |
| 23 | Email Auto Responder Flow | CrewAI | Communication | Automates email responses based on predefined criteria |
| 24 | Meeting Assistant Flow | CrewAI | Productivity | Organizes and manages meetings including scheduling |
| 25 | Self Evaluation Loop Flow | CrewAI | Human Resources | Facilitates self-assessment for performance reviews |
| 26 | Lead Score Flow | CrewAI | Sales | Evaluates and scores potential leads for outreach |
| 27 | Marketing Strategy Generator | CrewAI | Marketing | Develops marketing strategies from market trends |
| 28 | Job Posting Generator | CrewAI | Recruitment | Creates job postings by analyzing requirements |
| 29 | Recruitment Workflow | CrewAI | Recruitment | Streamlines recruitment by automating hiring tasks |
| 30 | Match Profile to Positions | CrewAI | Recruitment | Matches candidate profiles to suitable job positions |
| 31 | Instagram Post Generator | CrewAI | Social Media | Generates and schedules Instagram posts automatically |
| 32 | Landing Page Generator | CrewAI | Web Development | Automates creation of landing pages for websites |
| 33 | Game Builder Crew | CrewAI | Game Development | Assists in game development by automating creation |
| 34 | Stock Analysis Tool | CrewAI | Finance | Analyzes stock market data for financial decisions |
| 35 | Trip Planner | CrewAI | Travel | Assists in planning trips by organizing itineraries |
| 36 | Surprise Trip Planner | CrewAI | Travel | Plans surprise trips based on user preferences |
| 37 | Write a Book with Flows | CrewAI | Creative Writing | Assists authors in writing books with workflows |
| 38 | Screenplay Writer | CrewAI | Creative Writing | Aids in writing screenplays with templates and guidance |
| 39 | Markdown Validator | CrewAI | Documentation | Validates Markdown files for proper formatting |
| 40 | Meta Quest Knowledge | CrewAI | Knowledge Management | Manages knowledge related to Meta Quest |
| 41 | NVIDIA Models Integration | CrewAI | AI Integration | Integrates NVIDIA AI models into workflows |
| 42 | Prep for a Meeting | CrewAI | Productivity | Assists in preparing for meetings with agendas |
| 43 | Starter Template | CrewAI | Development | Provides a starter template for new projects |
| 44 | CrewAI + LangGraph Integration | CrewAI | AI Integration | Integrates CrewAI and LangGraph for workflow automation |
| 45 | Automated Task Solving with Code Gen, Execution & Debugging | AutoGen | Software Development | Automated task-solving by generating and debugging code |
| 46 | Code Generation with Retrieval Augmented Agents | AutoGen | Software Development | Generates code and answers questions using RAG |
| 47 | Code Generation with Qdrant-based Retrieval | AutoGen | Software Development | Qdrant-enhanced retrieval-augmented agent performance |
| 48 | Group Chat Task Solving (3 members, 1 manager) | AutoGen | Collaboration | Group task-solving via multi-agent collaboration |
| 49 | Data Visualization by Group Chat | AutoGen | Data Analysis | Multi-agent collaboration to create data visualizations |
| 50 | Complex Task Solving by Group Chat (6 members) | AutoGen | Collaboration | Solves complex tasks with larger group of agents |
| 51 | Task Solving with Coding & Planning Agents | AutoGen | Planning & Development | Combines coding and planning agents for task solving |
| 52 | Task Solving with Transition Paths in a Graph | AutoGen | Collaboration | Predefined transition paths in a graph for tasks |
| 53 | SocietyOfMindAgent Group Chat | AutoGen | Cognitive Sciences | Simulates inner-monologue via group chats |
| 54 | Group Chat with Custom Speaker Selection | AutoGen | Collaboration | Custom function for speaker selection in group chats |
| 55 | Sequential Multi-Task Chats (Single Agent) | AutoGen | Workflow Automation | Automates sequential task-solving with one agent |
| 56 | Async Sequential Multi-Task Chats | AutoGen | Workflow Automation | Asynchronous task-solving in a sequence of chats |
| 57 | Sequential Multi-Task Chats (Multiple Agents) | AutoGen | Workflow Automation | Sequential task-solving with different initiating agents |
| 58 | Nested Chats for Complex Tasks | AutoGen | Problem Solving | Uses nested chats to solve hierarchical problems |
| 59 | Sequence of Nested Chats | AutoGen | Problem Solving | Sequential task-solving using nested chats |
| 60 | OptiGuide Supply Chain with Nested Chats | AutoGen | Supply Chain Optimization | Supply chain optimization using nested chats |
| 61 | Conversational Chess with Nested Chats | AutoGen | Gaming | Conversational chess using nested chats and tools |
| 62 | Automated Continual Learning from New Data | AutoGen | Machine Learning | Continuously learns from new data inputs |
| 63 | OptiGuide - Supply Chain Optimization | AutoGen | Supply Chain Optimization | Coding, tool use, safeguarding for supply chain |
| 64 | AutoAnny - Discord Bot | AutoGen | Communication Tools | Discord bot built using AutoGen |
| 65 | Web Search: Solve Tasks Requiring Web Info | AutoGen | Information Retrieval | Searches the web to gather information for tasks |
| 66 | Use Provided Tools as Functions | AutoGen | Tool Integration | Uses pre-provided tools as callable functions |
| 67 | Sync and Async Function Calling | AutoGen | Tool Integration | Synchronous and asynchronous tool usage |
| 68 | Task Solving with Langchain Tools | AutoGen | Language Processing | Leverages Langchain tools for task-solving |
| 69 | RAG Group Chat | AutoGen | Collaboration | Group chat with Retrieval Augmented Generation |
| 70 | Function Inception: Update/Remove Functions | AutoGen | Development Tools | Agents modify their functions dynamically |
| 71 | Agent Chat with Whisper | AutoGen | Audio Processing | Transcription and translation using Whisper |
| 72 | Constrained Responses via Guidance | AutoGen | NLP | Uses guidance to constrain agent responses |
| 73 | Browse the Web with Agents | AutoGen | Information Retrieval | Agents browse and retrieve information from the web |
| 74 | SQL Natural Language to Query | AutoGen | Database Management | Converts natural language inputs into SQL queries |
| 75 | Web Scraping with Apify | AutoGen | Data Gathering | Web scraping with Apify using AutoGen |
| 76 | Web Crawling with Spider API | AutoGen | Data Gathering | Crawls entire domains using the Spider API |
| 77 | Write a Software App Task by Task | AutoGen | Software Development | Builds a software application step-by-step |
| 78 | Simple Example in ChatGPT Style | AutoGen | Conversational AI | Simple conversational example in ChatGPT style |
| 79 | Auto Code Gen, Execution, Debugging + Human Feedback | AutoGen | Software Development | Code generation with human feedback in workflow |
| 80 | Task Solving with GPT-4 + Multiple Human Users | AutoGen | Collaboration | Task solving with multiple human users and GPT-4 |
| 81 | Agent Chat with Async Human Inputs | AutoGen | Conversational AI | Asynchronous human input during agent conversations |
| 82 | Teach Agents New Skills via Automated Chat | AutoGen | Education & Training | Teaching new skills to agents for reuse in chats |
| 83 | Teach Agents Facts, Preferences and Skills | AutoGen | Education & Training | Teaches agents new facts, preferences, and skills |
| 84 | Teach OpenAI Assistants via GPTAssistantAgent | AutoGen | AI Assistant Development | Enhances OpenAI assistants via GPTAssistantAgent |
| 85 | Agent Optimizer: Train Agents Agentically | AutoGen | Optimization | Trains agents effectively in an agentic manner |
| 86 | Hello-World Chat with OpenAI Assistant | AutoGen | Conversational AI | Basic chat with OpenAI Assistant using AutoGen |
| 87 | Chat with OpenAI Assistant via Function Call | AutoGen | Development Tools | Function calls with OpenAI Assistant in chats |
| 88 | Chat with OpenAI Assistant + Code Interpreter | AutoGen | Software Development | OpenAI Assistant as a code interpreter |
| 89 | Chat with OpenAI Assistant + Retrieval Augmentation | AutoGen | Information Retrieval | Retrieval-augmented conversations with OpenAI Assistant |
| 90 | OpenAI Assistant in Group Chat | AutoGen | Collaboration | OpenAI Assistant collaborating with other agents |
| 91 | GPTAssistantAgent Multi-Agent Tool Use | AutoGen | Development Tools | GPTAssistantAgent for multi-agent tool usage |
| 92 | Conversational Chess (Non-OpenAI Models) | AutoGen | Gaming | Conversational chess with non-OpenAI models |
| 93 | Multimodal Agent Chat with DALLE and GPT-4V | AutoGen | Multimedia AI | Combines DALLE and GPT-4V for multimodal communication |
| 94 | Multimodal Agent Chat with Llava | AutoGen | Image Processing | Llava for multimodal agent conversations |
| 95 | Multimodal Agent Chat with GPT-4V | AutoGen | Multimedia AI | GPT-4V for visual and conversational interactions |
| 96 | Long Context Handling as A Capability | AutoGen | AI Capability | Techniques for handling long context in AI workflows |
| 97 | AgentEval: Multi-Agent LLM Assessment System | AutoGen | Performance Evaluation | Evaluates and assesses LLM-based applications |
| 98 | Automatically Build Multi-agent System (AgentBuilder) | AutoGen | AI Development | Automatically build multi-agent systems |
| 99 | Auto Build Multi-agent System from Agent Library | AutoGen | AI Development | Build multi-agent systems from a pre-defined library |
| 100 | Track LLM Calls with AgentOps | AutoGen | Monitoring & Analytics | Monitors LLM interactions, tool usage, and errors |
| 101 | API Unification | AutoGen | API Management | Unify API usage with documentation and code examples |
| 102 | Utility Functions for API Configuration | AutoGen | API Management | Utility functions to manage API configurations |
| 103 | Cost Calculation | AutoGen | Cost Management | Track token usage and estimate costs for LLMs |
| 104 | Optimize for Code Generation | AutoGen | Optimization | Cost-effective optimization for code generation |
| 105 | Optimize for Math | AutoGen | Optimization | Optimize LLM performance for mathematical problems |
| 106 | Support Agent | Agno | Software Development / AI | Real-time answers, explanations, and code examples |
| 107 | YouTube Agent | Agno | Media & Content | Analyzes YouTube videos with summaries and timestamps |
| 108 | Finance Agent (Thinking) | Agno | Finance | Real-time stock market insights and analyst recommendations |
| 109 | Study Partner | Agno | Education | Finds resources, answers questions, creates study plans |
| 110 | Shopping Partner Agent | Agno | E-commerce | Recommends products based on user preferences |
| 111 | Research Scholar Agent | Agno | Education / Research | Academic searches with synthesized findings and citations |
| 112 | Research Agent | Agno | Media & Journalism | Deep investigations producing NYT-style reports |
| 113 | Recipe Creator | Agno | Food & Culinary | Personalized recipes based on ingredients and preferences |
| 114 | Finance Agent | Agno | Finance | Financial analyst combining stock data and market news |
| 115 | Financial Reasoning Agent | Agno | Finance | Claude-3.5 Sonnet-based stock analysis with reasoning |
| 116 | Readme Generator Agent | Agno | Software Development | Generates READMEs for GitHub repositories |
| 117 | Movie Recommendation Agent | Agno | Entertainment | Personalized movie recommendations using Exa and GPT-4o |
| 118 | Media Trend Analysis Agent | Agno | Media & News | Analyzes trends and influencers from digital platforms |
| 119 | Legal Document Analysis Agent | Agno | Legal Tech | Analyzes legal documents from PDF URLs with AI insights |
| 120 | DeepKnowledge | Agno | Research | Iterative knowledge base searches for complex queries |
| 121 | Book Recommendation Agent | Agno | Publishing & Media | Personalized book suggestions using literary data |
| 122 | MCP Airbnb Agent | Agno | Hospitality | Searches Airbnb listings with MCP and Llama 4 |
| 123 | Agno Assist Agent | Agno | AI Framework | Answers Agno framework questions with hybrid search |
| 124 | Chatbot Simulation Evaluation | LangGraph | AI / QA | Simulates user interactions to evaluate chatbot performance |
| 125 | Information Gathering via Prompting | LangGraph | AI / Research | LangGraph workflow for structured information gathering |
| 126 | Code Assistant with LangGraph | LangGraph | Software Development | Graph-based agent for code generation and refinement |
| 127 | Customer Support Agent | LangGraph | Customer Support | Graph-based agent for handling customer inquiries |
| 128 | Extraction with Retries | LangGraph | AI / Data Extraction | Retry mechanisms for robust data extraction |
| 129 | Multi-Agent Workflow | LangGraph | AI / Workflow Orchestration | Supervisor agent orchestrating multiple specialized agents |
| 130 | Hierarchical Agent Teams | LangGraph | AI / Workflow Orchestration | Top-level supervisor delegating to specialized sub-agents |
| 131 | Multi-Agent Collaboration | LangGraph | AI / Workflow Orchestration | Multiple specialized agents working together |
| 132 | Plan-and-Execute Agent | LangGraph | AI / Workflow Orchestration | Agent that generates a multi-step plan and executes it |
| 133 | SQL Agent | LangGraph | AI / Database Interaction | Agent that answers questions about SQL databases |
| 134 | Reflection Agent | LangGraph | AI / Workflow Orchestration | Agent that critiques and revises its own outputs |
| 135 | Reflexion Agent | LangGraph | AI / Workflow Orchestration | Agent reflecting on actions for iterative improvement |
| 136 | Adaptive RAG | LangGraph | AI / Information Retrieval | Dynamic retrieval adjusting based on query complexity |
| 137 | Adaptive RAG (Local) | LangGraph | AI / Information Retrieval | Adaptive RAG with local models for offline use |
| 138 | Agentic RAG | LangGraph | AI / Intelligent Agents | Agent determines best retrieval strategy before generating |
| 139 | Agentic RAG (Local) | LangGraph | AI / Intelligent Agents | Agentic RAG extended to local environments |
| 140 | Corrective RAG (CRAG) | LangGraph | AI / Information Retrieval | Evaluates and refines retrieved documents before generation |
| 141 | Corrective RAG (Local) | LangGraph | AI / Information Retrieval | Corrective RAG using local resources |
| 142 | Self-RAG | LangGraph | AI / Information Retrieval | System reflects on responses and retrieves extra info |
| 143 | Self-RAG (Local) | LangGraph | AI / Information Retrieval | Self-RAG with local models for offline reflection |

---

## 1. Industry Use Cases

22 agents spanning 15+ industries, each linking to an open-source implementation.

| Use Case | Industry | Description | Code |
|----------|----------|-------------|------|
| **HIA (Health Insights Agent)** | Healthcare | Analyses medical reports and provide health insights. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/harshhh28/hia.git) |
| **AI Health Assistant** | Healthcare | Diagnoses and monitors diseases using patient data. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/ahmadvh/AI-Agents-for-Medical-Diagnostics.git) |
| **Automated Trading Bot** | Finance | Automates stock trading with real-time market analysis. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/MingyuJ666/Stockagent.git) |
| **Virtual AI Tutor** | Education | Provides personalized education tailored to users. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/hqanhh/EduGPT.git) |
| **24/7 AI Chatbot** | Customer Service | Handles customer queries around the clock. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/NirDiamant/GenAI_Agents/blob/main/all_agents_tutorials/customer_support_agent_langgraph.ipynb) |
| **Product Recommendation Agent** | Retail | Suggests products based on user preferences and history. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/microsoft/RecAI) |
| **Self-Driving Delivery Agent** | Transportation | Optimizes routes and autonomously delivers packages. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/sled-group/driVLMe) |
| **Factory Process Monitoring Agent** | Manufacturing | Monitors production lines and ensures quality control. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/yuchenxia/llm4ias) |
| **Property Pricing Agent** | Real Estate | Analyzes market trends to determine property prices. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/AleksNeStu/ai-real-estate-assistant) |
| **Smart Farming Assistant** | Agriculture | Provides insights on crop health and yield predictions. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/mohammed97ashraf/LLM_Agri_Bot) |
| **Energy Demand Forecasting Agent** | Energy | Predicts energy usage to optimize grid management. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/yecchen/MIRAI) |
| **Content Personalization Agent** | Entertainment | Recommends personalized media based on preferences. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/crosleythomas/MirrorGPT) |
| **Legal Document Review Assistant** | Legal | Automates document review and highlights key clauses. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/firica/legalai) |
| **Recruitment Recommendation Agent** | Human Resources | Suggests best-fit candidates for job openings. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/sentient-engineering/jobber) |
| **Virtual Travel Assistant** | Hospitality | Plans travel itineraries based on preferences. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/nirbar1985/ai-travel-agent) |
| **AI Game Companion Agent** | Gaming | Enhances player experience with real-time assistance. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/onjas-buidl/LLM-agent-game) |
| **Real-Time Threat Detection Agent** | Cybersecurity | Identifies potential threats and mitigates attacks. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/NVISOsecurity/cyber-security-llm-agents) |
| **E-commerce Personal Shopper Agent** | E-commerce | Helps customers find products they'll love. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/Hoanganhvu123/ShoppingGPT) |
| **Logistics Optimization Agent** | Supply Chain | Plans efficient delivery routes and manages inventory. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/microsoft/OptiGuide) |
| **Vibe Hacking Agent** | Cybersecurity | Autonomous Multi-Agent Based Red Team Testing Service. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/PurpleAILAB/Decepticon) |
| **MediSuite-Ai-Agent** | Health Insurance | Automates hospital/insurance claiming workflow. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/MahmoudRabea13/MediSuite-Ai-Agent) |
| **Lina-Egyptian-Medical-Chatbot** | Health Insurance | AI medical chatbot for hospital/insurance workflow. | [![GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github)](https://github.com/MahmoudRabea13/MediSuite-Ai-Agent) |

---

## 2. CrewAI Agents

22 agents built with the [CrewAI](https://github.com/crewAIInc/crewAI) framework, covering communication, productivity, recruitment, marketing, creative writing, and more.

| Use Case | Industry | Description | GitHub |
|----------|----------|-------------|--------|
| 📧 Email Auto Responder Flow | Communication | Automates email responses based on predefined criteria to enhance communication efficiency. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/email_auto_responder_flow) |
| 📝 Meeting Assistant Flow | Productivity | Assists in organizing and managing meetings, including scheduling and agenda preparation. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/meeting_assistant_flow) |
| 🔄 Self Evaluation Loop Flow | Human Resources | Facilitates self-assessment processes within an organization, aiding in performance reviews. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/self_evaluation_loop_flow) |
| 📈 Lead Score Flow | Sales | Evaluates and scores potential leads to prioritize outreach in sales strategies. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/lead-score-flow) |
| 📊 Marketing Strategy Generator | Marketing | Develops marketing strategies by analyzing market trends and audience data. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/marketing_strategy) |
| 📝 Job Posting Generator | Recruitment | Creates job postings by analyzing job requirements, aiding in recruitment processes. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/job-posting) |
| 🔄 Recruitment Workflow | Recruitment | Streamlines the recruitment process by automating various tasks involved in hiring. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/recruitment) |
| 🔍 Match Profile to Positions | Recruitment | Matches candidate profiles to suitable job positions to enhance recruitment efficiency. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/match_profile_to_positions) |
| 📸 Instagram Post Generator | Social Media | Generates and schedules Instagram posts automatically, streamlining social media management. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/instagram_post) |
| 🌐 Landing Page Generator | Web Development | Automates the creation of landing pages for websites, facilitating web development tasks. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/landing_page_generator) |
| 🎮 Game Builder Crew | Game Development | Assists in the development of games by automating certain aspects of game creation. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/game-builder-crew) |
| 💹 Stock Analysis Tool | Finance | Provides tools for analyzing stock market data to assist in financial decision-making. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis) |
| 🗺️ Trip Planner | Travel | Assists in planning trips by organizing itineraries and managing travel details. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner) |
| 🎁 Surprise Trip Planner | Travel | Plans surprise trips by selecting destinations and activities based on user preferences. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/surprise_trip) |
| 📚 Write a Book with Flows | Creative Writing | Assists authors in writing books by providing structured workflows and writing assistance. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/flows/write_a_book_with_flows) |
| 🎬 Screenplay Writer | Creative Writing | Aids in writing screenplays by offering templates and guidance for script development. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/screenplay_writer) |
| ✅ Markdown Validator | Documentation | Validates Markdown files to ensure proper formatting and adherence to standards. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/markdown_validator) |
| 🧠 Meta Quest Knowledge | Knowledge Management | Manages and organizes knowledge related to Meta Quest, facilitating information retrieval. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/meta_quest_knowledge) |
| 🤖 NVIDIA Models Integration | AI Integration | Integrates NVIDIA AI models into workflows to enhance computational capabilities. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/nvidia_models) |
| 🗂️ Prep for a Meeting | Productivity | Assists in preparing for meetings by organizing materials and setting agendas. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/prep-for-a-meeting) |
| 🛠️ Starter Template | Development | Provides a starter template for new projects to streamline the setup process. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/starter_template) |
| 🔗 CrewAI + LangGraph Integration | AI Integration | Demonstrates integration between CrewAI and LangGraph for enhanced workflow automation. | [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/crewAIInc/crewAI-examples/tree/main/integrations/CrewAI-LangGraph) |

---

## 3. AutoGen Agents

~50 agents built with [Microsoft AutoGen](https://github.com/microsoft/autogen), organized by capability category.

### Code Generation, Execution, and Debugging

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🤖 Automated Task Solving with Code Generation, Execution & Debugging | Software Development | Demonstrates automated task-solving by generating, executing, and debugging code. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_auto_feedback_from_code_execution) |
| 🧑‍💻 Automated Code Generation and Question Answering with Retrieval Augmented Agents | Software Development | Generates code and answers questions using retrieval-augmented methods. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_RetrieveChat) |
| 🧠 Automated Code Generation and Question Answering with Qdrant-based Retrieval | Software Development | Utilizes Qdrant for enhanced retrieval-augmented agent performance. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_RetrieveChat_qdrant) |

### Multi-Agent Collaboration (3+ Agents)

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🤝 Automated Task Solving by Group Chat (3 members, 1 manager) | Collaboration | Demonstrates group task-solving via multi-agent collaboration. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat) |
| 📊 Automated Data Visualization by Group Chat (3 members, 1 manager) | Data Analysis | Uses multi-agent collaboration to create data visualizations. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_vis) |
| 🧩 Automated Complex Task Solving by Group Chat (6 members, 1 manager) | Collaboration | Solves complex tasks collaboratively with a larger group of agents. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_research) |
| 🧑‍💻 Automated Task Solving with Coding & Planning Agents | Planning & Development | Combines coding and planning agents for solving tasks effectively. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_planning.ipynb) |
| 📐 Automated Task Solving with Transition Paths Specified in a Graph | Collaboration | Uses predefined transition paths in a graph for solving tasks. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/docs/notebooks/agentchat_groupchat_finite_state_machine) |
| 🧠 Running a Group Chat as an Inner-Monologue via the SocietyOfMindAgent | Cognitive Sciences | Simulates inner-monologue for problem-solving using group chats. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_society_of_mind) |
| 🔧 Running a Group Chat with Custom Speaker Selection Function | Collaboration | Implements a custom function for speaker selection in group chats. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_customized) |

### Sequential Multi-Agent Chats

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🔄 Solving Multiple Tasks in a Sequence of Chats Initiated by a Single Agent | Workflow Automation | Automates sequential task-solving with a single initiating agent. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_multi_task_chats) |
| ⏳ Async-solving Multiple Tasks in a Sequence of Chats Initiated by a Single Agent | Workflow Automation | Handles asynchronous task-solving in a sequence of chats initiated by one agent. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_multi_task_async_chats) |
| 🤝 Solving Multiple Tasks in a Sequence of Chats Initiated by Different Agents | Workflow Automation | Facilitates sequential task-solving with different agents initiating each chat. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchats_sequential_chats) |

### Nested Chats

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🧠 Solving Complex Tasks with Nested Chats | Problem Solving | Uses nested chats to solve hierarchical and complex problems. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nestedchat) |
| 🔄 Solving Complex Tasks with A Sequence of Nested Chats | Problem Solving | Demonstrates sequential task-solving using nested chats. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nested_sequential_chats) |
| 🏭 OptiGuide for Supply Chain Optimization with Nested Chats | Supply Chain Optimization | Showcases supply chain optimization using nested chats, a coding agent, and a safeguard agent. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nestedchat_optiguide) |
| ♟️ Conversational Chess with Nested Chats and Tool Use | Gaming | Explores nested chats for playing conversational chess with integrated tools. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nested_chats_chess) |

### Application

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🔄 Automated Continual Learning from New Data | Machine Learning | Continuously learns from new data inputs for adaptive AI. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_stream.ipynb) |
| 🏭 OptiGuide - Coding, Tool Using, Safeguarding & QA for Supply Chain | Supply Chain Optimization | Solution combining coding, tool use, and safeguarding for supply chain optimization. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nestedchat_optiguide) |
| 🤖 AutoAnny - A Discord Bot Built Using AutoGen | Communication Tools | Showcases the development of a Discord bot using AutoGen for enhanced interaction. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/tree/main/samples/apps/auto-anny) |

### Tools

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🌐 Web Search: Solve Tasks Requiring Web Info | Information Retrieval | Searches the web to gather information required for completing tasks. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_web_info.ipynb) |
| 🔧 Use Provided Tools as Functions | Tool Integration | Demonstrates how to use pre-provided tools as callable functions in AutoGen. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_function_call_currency_calculator) |
| 🔗 Use Tools via Sync and Async Function Calling | Tool Integration | Illustrates synchronous and asynchronous tool usage within AutoGen workflows. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_function_call_async) |
| 🧩 Task Solving with Langchain Provided Tools as Functions | Language Processing | Leverages Langchain tools for task-solving within AutoGen. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_langchain.ipynb) |
| 📚 RAG: Group Chat with Retrieval Augmented Generation | Collaboration | Enables group chat with RAG to support information sharing. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_RAG) |
| ⚙️ Function Inception: Update/Remove Functions During Conversations | Development Tools | Allows AutoGen agents to modify their functions dynamically during conversations. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_inception_function.ipynb) |
| 🔊 Agent Chat with Whisper | Audio Processing | Demonstrates AI agent capabilities for transcription and translation using Whisper. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_video_transcript_translate_with_whisper) |
| 📏 Constrained Responses via Guidance | NLP | Shows how to use guidance to constrain responses generated by agents. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_guidance.ipynb) |
| 🌍 Browse the Web with Agents | Information Retrieval | Explains how to configure agents to browse and retrieve information from the web. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_surfer.ipynb) |
| 📊 SQL: Natural Language Text to SQL Query Using Spider Benchmark | Database Management | Converts natural language inputs into SQL queries using the Spider benchmark. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_sql_spider.ipynb) |
| 🕸️ Web Scraping with Apify | Data Gathering | Illustrates web scraping techniques with Apify using AutoGen. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_webscraping_with_apify) |
| 🕷️ Web Crawling: Crawl Entire Domain with Spider API | Data Gathering | Explains how to crawl entire domains using the Spider API. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_webcrawling_with_spider) |
| 💻 Write a Software App Task by Task with Specially Designed Functions | Software Development | Builds a software application step-by-step using designed functions. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_function_call_code_writing.ipynb) |

### Human Development

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 💬 Simple Example in ChatGPT Style | Conversational AI | Demonstrates a simple conversational example in the style of ChatGPT. | [![Example](https://img.shields.io/badge/View-Example-blue?logo=openai)](https://github.com/microsoft/autogen/blob/0.2/samples/simple_chat.py) |
| 🤖 Auto Code Generation, Execution, Debugging and Human Feedback | Software Development | Showcases code generation, execution, debugging with human feedback in the workflow. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_human_feedback.ipynb) |
| 👥 Automated Task Solving with GPT-4 + Multiple Human Users | Collaboration | Enables task solving with multiple human users collaborating with GPT-4. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_two_users.ipynb) |
| 🔄 Agent Chat with Async Human Inputs | Conversational AI | Supports asynchronous human input during agent conversations. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/Async_human_input.ipynb) |

### Agent Teaching and Learning

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 📘 Teach Agents New Skills & Reuse via Automated Chat | Education & Training | Demonstrates teaching new skills to agents and enabling their reuse in automated chats. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_teaching) |
| 🧠 Teach Agents New Facts, User Preferences and Skills Beyond Coding | Education & Training | Shows how to teach agents new facts, user preferences, and non-coding skills. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_teachability) |
| 🤖 Teach OpenAI Assistants Through GPTAssistantAgent | AI Assistant Development | Illustrates how to enhance OpenAI assistants' capabilities using GPTAssistantAgent. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_teachable_oai_assistants.ipynb) |
| 🔄 Agent Optimizer: Train Agents in an Agentic Way | Optimization | Explains how to train agents effectively in an agentic manner using the Agent Optimizer. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_agentoptimizer.ipynb) |

### Multi-Agent Chat with OpenAI Assistants

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🌟 Hello-World Chat with OpenAI Assistant in AutoGen | Conversational AI | A basic example of chatting with OpenAI Assistant using AutoGen. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_assistant_twoagents_basic.ipynb) |
| 🔧 Chat with OpenAI Assistant using Function Call | Development Tools | Illustrates how to use function calls with OpenAI Assistant in chats. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_assistant_function_call.ipynb) |
| 🧠 Chat with OpenAI Assistant with Code Interpreter | Software Development | Demonstrates the use of OpenAI Assistant as a code interpreter in chats. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_code_interpreter.ipynb) |
| 🔍 Chat with OpenAI Assistant with Retrieval Augmentation | Information Retrieval | Enables retrieval-augmented conversations with OpenAI Assistant. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_assistant_retrieval.ipynb) |
| 🤝 OpenAI Assistant in a Group Chat | Collaboration | Shows how OpenAI Assistant can collaborate with other agents in a group chat. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_oai_assistant_groupchat.ipynb) |
| 🛠️ GPTAssistantAgent based Multi-Agent Tool Use | Development Tools | Explains how to use GPTAssistantAgent for multi-agent tool usage. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/gpt_assistant_agent_function_call.ipynb) |

### Non-OpenAI Models

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| ♟️ Conversational Chess using Non-OpenAI Models | Gaming | Explores conversational chess implemented with non-OpenAI models. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_nested_chats_chess_altmodels) |

### Multimodal Agent

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🎨 Multimodal Agent Chat with DALLE and GPT-4V | Multimedia AI | Combines DALLE and GPT-4V for multimodal agent communication. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_dalle_and_gpt4v.ipynb) |
| 🖌️ Multimodal Agent Chat with Llava | Image Processing | Uses Llava for enabling multimodal agent conversations with image processing. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_lmm_llava.ipynb) |
| 🖼️ Multimodal Agent Chat with GPT-4V | Multimedia AI | Leverages GPT-4V for visual and conversational interactions in multimodal agents. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_lmm_gpt-4v.ipynb) |

### Long Context Handling

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 📜 Long Context Handling as A Capability | AI Capability | Demonstrates techniques for handling long context effectively within AI workflows. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_transform_messages) |

### Evaluation and Assessment

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 📊 AgentEval: A Multi-Agent System for Assessing Utility of LLM-Powered Applications | Performance Evaluation | Introduces AgentEval for evaluating and assessing the performance of LLM-based applications. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agenteval_cq_math.ipynb) |

### Automatic Agent Building

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🏗️ Automatically Build Multi-agent System with AgentBuilder | AI Development | Explains how to automatically build multi-agent systems using the AgentBuilder tool. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/autobuild_basic.ipynb) |
| 📚 Automatically Build Multi-agent System from Agent Library | AI Development | Shows how to construct multi-agent systems by leveraging a pre-defined agent library. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/autobuild_agent_library.ipynb) |

### Observability

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 📊 Track LLM Calls, Tool Usage, Actions and Errors using AgentOps | Monitoring & Analytics | Demonstrates how to monitor LLM interactions, tool usage, and errors using AgentOps. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_agentops.ipynb) |

### Enhanced Inferences

| Use Case | Industry | Description | Notebook |
|----------|----------|-------------|----------|
| 🔗 API Unification | API Management | Explains how to unify API usage with documentation and code examples. | [![Documentation](https://img.shields.io/badge/View-Documentation-blue?logo=readthedocs)](https://microsoft.github.io/autogen/docs/Use-Cases/enhanced_inference/#api-unification) |
| ⚙️ Utility Functions to Help Managing API Configurations Effectively | API Management | Demonstrates utility functions to manage API configurations more effectively. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://microsoft.github.io/autogen/0.2/docs/topics/llm_configuration) |
| 💰 Cost Calculation | Cost Management | Introduces methods for tracking token usage and estimating costs for LLM interactions. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_cost_token_tracking.ipynb) |
| ⚡ Optimize for Code Generation | Optimization | Highlights cost-effective optimization techniques for improving code generation with LLMs. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/oai_completion.ipynb) |
| 📐 Optimize for Math | Optimization | Explains techniques to optimize LLM performance for solving mathematical problems. | [![Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://github.com/microsoft/autogen/blob/0.2/notebook/oai_chatgpt_gpt4.ipynb) |

---

## 4. Agno Agents

18 agents built with the [Agno](https://github.com/agno-agi/agno) framework, covering finance, education, media, legal, and more.

| Use Case | Industry | Description | Code |
|----------|----------|-------------|------|
| 🤖 Support Agent | Software Development / AI | Helps developers with the Agno framework by providing real-time answers, explanations, and code examples. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/agno_support_agent.py) |
| 🎥 YouTube Agent | Media & Content | Analyzes YouTube videos by generating summaries, timestamps, themes, and content breakdowns. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/youtube_agent.py) |
| 📊 Finance Agent (Thinking) | Finance | Delivers real-time stock market insights, analyst recommendations, and sector-specific trends. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/thinking_finance_agent.py) |
| 📚 Study Partner | Education | Assists users in learning by finding resources, answering questions, and creating study plans. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/study_partner.py) |
| 🛍️ Shopping Partner Agent | E-commerce | Recommends products based on preferences from trusted platforms like Amazon and Flipkart. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/shopping_partner.py) |
| 🎓 Research Scholar Agent | Education / Research | Performs academic searches, analyzes publications, synthesizes findings, and writes cited reports. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/research_agent_exa.py) |
| 🧠 Research Agent | Media & Journalism | Combines web search and professional journalistic writing for deep investigations. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/research_agent.py) |
| 🍳 Recipe Creator | Food & Culinary | Provides personalized recipes based on ingredients, preferences, and time constraints. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/recipe_creator.py) |
| 🗞️ Finance Agent | Finance | Financial analyst combining real-time stock data, analyst insights, and market news. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/finance_agent.py) |
| 🧠 Financial Reasoning Agent | Finance | Claude-3.5 Sonnet-based agent for stock analysis using reasoning and Yahoo Finance data. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/reasoning_finance_agent.py) |
| 🤖 Readme Generator Agent | Software Development | Generates high-quality READMEs for GitHub repositories using repo metadata. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/readme_generator.py) |
| 🎬 Movie Recommendation Agent | Entertainment | Gives personalized movie recommendations using Exa and GPT-4o. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/movie_recommedation.py) |
| 🔍 Media Trend Analysis Agent | Media & News | Analyzes emerging trends, patterns, and influencers from digital platforms. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/media_trend_analysis_agent.py) |
| ⚖️ Legal Document Analysis Agent | Legal Tech | Analyzes legal documents from PDF URLs and provides legal insights via vector embeddings. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/legal_consultant.py) |
| 🤔 DeepKnowledge | Research | Iterative knowledge base searches, breaking complex queries into sub-questions. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/deep_knowledge.py) |
| 📚 Book Recommendation Agent | Publishing & Media | Personalized book suggestions using literary data, reader preferences, and reviews. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/book_recommendation.py) |
| 🏠 MCP Airbnb Agent | Hospitality | Searches Airbnb listings with MCP and Llama 4 with workspace and transport filters. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/airbnb_mcp.py) |
| 🤖 Agno Assist Agent | AI Framework | Answers Agno framework questions with hybrid search and embedded knowledge via GPT-4o. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/agno_assist.py) |

---

## 5. LangGraph Agents

22 agents built with [LangGraph](https://github.com/langchain-ai/langgraph), including core agent patterns and an 8-variant RAG section.

### Core Agents

| Use Case | Industry | Description | Code |
|----------|----------|-------------|------|
| 🤖 Chatbot Simulation Evaluation | AI / Quality Assurance | Simulate user interactions to evaluate chatbot performance for robustness. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/chatbot-simulation-evaluation/agent-simulation-evaluation.ipynb) |
| 🧠 Information Gathering via Prompting | AI / Research & Development | LangGraph workflow using prompting techniques to gather information effectively. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/chatbots/information-gather-prompting.ipynb) |
| 🧠 Code Assistant with LangGraph | Software Development | Graph-based agent for code generation, error checking, and iterative refinement. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/code_assistant/langgraph_code_assistant.ipynb) |
| 🧑‍💼 Customer Support Agent | Customer Support | Graph-based agent for handling customer inquiries and providing automated support. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/customer-support/customer-support.ipynb) |
| 🔁 Extraction with Retries | AI / Data Extraction | Retry mechanisms ensuring robust data extraction processes with transient error handling. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/extraction/retries.ipynb) |
| 🧠 Multi-Agent Workflow | AI / Workflow Orchestration | Supervisor agent orchestrating multiple specialized agents with task delegation. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/agent_supervisor.ipynb) |
| 🧠 Hierarchical Agent Teams | AI / Workflow Orchestration | Top-level supervisor agent delegating tasks to specialized sub-agents. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/hierarchical_agent_teams.ipynb) |
| 🤝 Multi-Agent Collaboration | AI / Workflow Orchestration | Multiple specialized agents working together to accomplish complex tasks. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/multi_agent/multi-agent-collaboration.ipynb) |
| 🧠 Plan-and-Execute Agent | AI / Workflow Orchestration | Agent that generates a multi-step plan and executes each step sequentially. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/plan-and-execute/plan-and-execute.ipynb) |
| 🧠 SQL Agent | AI / Database Interaction | Agent that fetches tables, generates queries, checks errors, and formulates responses. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/sql-agent.ipynb) |
| 🧠 Reflection Agent | AI / Workflow Orchestration | Agent that critiques and revises its own outputs for enhanced quality. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/reflection/reflection.ipynb) |
| 🧠 Reflexion Agent | AI / Workflow Orchestration | Agent that reflects on its actions and outcomes for iterative improvement. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/reflexion/reflexion.ipynb) |

### Agentic RAG Variants

| Use Case | Industry | Description | Code |
|----------|----------|-------------|------|
| 🧠 Adaptive RAG | AI / Information Retrieval | Dynamic retrieval adjusting based on query complexity for efficient information retrieval. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_adaptive_rag.ipynb) |
| 🧠 Adaptive RAG (Local) | AI / Information Retrieval | Adaptive RAG with local models for offline retrieval and privacy-sensitive environments. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_adaptive_rag_local.ipynb) |
| 🤖 Agentic RAG | AI / Intelligent Agents | Agent determines the best retrieval strategy before generating a response. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_agentic_rag.ipynb) |
| 🤖 Agentic RAG (Local) | AI / Intelligent Agents | Agentic RAG extended to local environments with local models and data sources. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_agentic_rag_local.ipynb) |
| 🧠 Corrective RAG (CRAG) | AI / Information Retrieval | Evaluates and refines retrieved documents before passing them to the generator. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_crag.ipynb) |
| 🧠 Corrective RAG (Local) | AI / Information Retrieval | Corrective RAG using local resources for offline document evaluation. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_crag_local.ipynb) |
| 🧠 Self-RAG | AI / Information Retrieval | System reflects on its responses and retrieves additional information if necessary. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_self_rag.ipynb) |
| 🧠 Self-RAG (Local) | AI / Information Retrieval | Self-RAG with local models and data sources for offline reflection and retrieval. | [![Python](https://img.shields.io/static/v1?label=AI+Agent+Code&message=Python&color=%23244cd1)](https://github.com/langchain-ai/langgraph/blob/main/docs/docs/tutorials/rag/langgraph_self_rag_local.ipynb) |

---

## Contributing

See [CONTRIBUTION.md](CONTRIBUTION.md) for how to add new agents, required folder structure, metadata schema, naming conventions, and the PR checklist.
