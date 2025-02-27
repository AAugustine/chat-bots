import express from 'express';
import ImageController from '../controllers/imageController.js';

const router = express.Router();
const imageController = new ImageController();

// Add a test route
router.get('/test', (req, res) => {
    res.json({ message: 'Image routes are working!' });
});

// Route to handle image generation
router.post('/generate', (req, res) => imageController.generateImage(req, res));

export default router;