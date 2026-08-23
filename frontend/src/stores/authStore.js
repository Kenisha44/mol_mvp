import { writable } from 'svelte/store';
import { supabase } from '../lib/supabaseClient.js';

export const passwordRecovery = writable(false);
export const user = writable(null);
export const authLoading = writable(true);

export async function initializeAuth() {
  const {
    data: { session },
    error
  } = await supabase.auth.getSession();

  if (error) {
    console.error('Unable to load auth session:', error);
  }

  user.set(session?.user ?? null);
  authLoading.set(false);

  supabase.auth.onAuthStateChange((event, session) => {
    user.set(session?.user ?? null);
  
    if (event === 'PASSWORD_RECOVERY') {
      passwordRecovery.set(true);
    }
  });
}