import { Router, Request, Response } from 'express';
import { generateTestCases } from '../services/llmService';

const router = Router();

router.post('/', async (req: Request, res: Response) => {
  try {
    const { requirement, settings } = req.body;

    if (!requirement) {
       return res.status(400).json({ error: 'Requirement text is required.' });
    }

    if (!settings || !settings.provider) {
       return res.status(400).json({ error: 'LLM Settings (provider) are required.' });
    }

    const testCases = await generateTestCases(requirement, settings);
    
    res.json({ success: true, data: testCases });
  } catch (error: any) {
    console.error('Error generating test cases:', error);
    res.status(500).json({ success: false, error: error.message || 'An unexpected error occurred.' });
  }
});

export default router;
