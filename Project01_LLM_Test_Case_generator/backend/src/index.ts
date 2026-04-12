import express, { Request, Response } from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import generateRoute from './routes/generate';

dotenv.config();

const app = express();
const port = process.env.PORT || 3001;

app.use(cors());
app.use(express.json());

// Routes
app.use('/api/generate', generateRoute);

app.get('/health', (req: Request, res: Response) => {
  res.json({ status: 'ok', message: 'LocalLLMTestGenBuddy Backend is running' });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
