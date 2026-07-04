import { apiPost } from '../../lib/api.js';

export async function analyzeClarity(text) {
  return apiPost('/clarity/analyze', { text });
}