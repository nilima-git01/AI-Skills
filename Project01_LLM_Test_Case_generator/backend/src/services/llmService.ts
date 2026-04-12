import { generateWithOllama } from './providers/ollama';

// Settings interface matching what the frontend will send
export interface LLMSettings {
  provider: 'ollama' | 'lmstudio' | 'openai' | 'claude' | 'grok' | 'gemini';
  modelUrl?: string; // e.g., http://localhost:11434 for Ollama
  modelName: string; // e.g., llama3, gpt-4
  apiKey?: string;
}

const SYSTEM_PROMPT = `
You are an expert QA Engineer. The user will provide you with a software requirement (often in Jira format).
Your task is to generate both Functional and Non-functional test cases based on this requirement.

CRITICAL INSTRUCTION: You MUST output the final result STRICTLY as a single Markdown table.
Do NOT output any conversational text before or after the table. Only the Markdown table.

The table must have the following columns:
| Test Case ID | Test Category (Functional/Non-Functional) | Test Scenario | Preconditions | Test Steps | Expected Result | Priority |

Ensure you generate comprehensive edge cases for both Web Applications and APIs based on the context.
`.trim();

export const generateTestCases = async (requirement: string, settings: LLMSettings): Promise<string> => {
  
  const prompt = `${SYSTEM_PROMPT}\n\nUSER REQUIREMENT:\n${requirement}`;

  switch (settings.provider) {
    case 'ollama':
      return await generateWithOllama(prompt, settings);
    case 'lmstudio':
      // Placeholder for LM Studio implementation
      throw new Error("LM Studio provider not yet implemented.");
    case 'openai':
      throw new Error("OpenAI provider not yet implemented.");
    case 'claude':
        throw new Error("Claude provider not yet implemented.");
    case 'grok':
        throw new Error("Grok provider not yet implemented.");
    case 'gemini':
        throw new Error("Gemini provider not yet implemented.");
    default:
      throw new Error(`Unsupported LLM provider: ${settings.provider}`);
  }
};
