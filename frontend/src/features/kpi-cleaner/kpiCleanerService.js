import { apiPost } from '../../lib/api.js';

export async function cleanKpi(text) {
  return apiPost('/kpi-cleaner/clean', { text });
}