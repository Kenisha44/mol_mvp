import { API_BASE } from './apiConfig.js';
import {
  canRunAnalysis,
  recordAnalysisUsage
} from './usageService.js';

export async function apiPost(endpoint, payload) {
  const usageCheck = canRunAnalysis();

  if (!usageCheck.allowed) {
    throw new Error(usageCheck.reason);
  }

  const response = await fetch(`${API_BASE}${endpoint}`, {
    method: 'POST',

    headers: {
      'Content-Type': 'application/json'
    },

    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    throw new Error('Backend error');
  }

  const data = await response.json();

  await recordAnalysisUsage();

  return data;
}