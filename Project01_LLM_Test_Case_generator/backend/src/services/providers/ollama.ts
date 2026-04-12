import axios from 'axios';
import { LLMSettings } from '../llmService';

export const generateWithOllama = async (prompt: string, settings: LLMSettings): Promise<string> => {
  const baseUrl = settings.modelUrl || 'http://127.0.0.1:11434';
  const url = `${baseUrl}/api/generate`;

  try {
    const response = await axios.post(url, {
      model: settings.modelName || 'llama3', // Default to llama3 if unset, up to user
      prompt: prompt,
      stream: false,
    });

    if (response.data && response.data.response) {
      return response.data.response;
    } else {
      throw new Error('Unexpected response format from Ollama API.');
    }
  } catch (error: any) {
    console.error('Ollama connection error:', error.message);
    if (error.code === 'ECONNREFUSED') {
         throw new Error(`Failed to connect to Ollama at ${baseUrl}. Ensure it is running (ollama serve).`);
    }
    throw new Error(`Ollama Generation Error: ${error.message}`);
  }
};
