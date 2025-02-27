import OpenAI from 'openai';
import dotenv from 'dotenv';

dotenv.config();

const openai = new OpenAI({
  apiKey: process.env.API_KEY,
});

class ImageController {
  async generateImage(req, res) {
    try {
      const { prompt } = req.body;
      
      if (!prompt) {
        return res.status(400).json({ error: 'Prompt is required' });
      }

      const response = await openai.images.generate({
        model: "dall-e-3",
        prompt: prompt,
        n: 1,
        size: "1024x1024",
      });

      return res.json({ 
        success: true, 
        imageUrl: response.data[0].url 
      });

    } catch (error) {
      console.error('Error generating image:', error);
      return res.status(500).json({ 
        error: 'Failed to generate image',
        details: error.message 
      });
    }
  }
}

export default ImageController;