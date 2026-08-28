import { writable } from 'svelte/store';
import { supabase } from '../lib/supabaseClient.js';
import {
  loadProfile,
  clearProfile
} from './profileStore.js';

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

  if (session?.user) {
    await loadProfile();
  } else {
    clearProfile();
  }
  
  authLoading.set(false);

  supabase.auth.onAuthStateChange(
    async (event, session) => {
  
      user.set(session?.user ?? null);
  
      if (event === 'PASSWORD_RECOVERY') {
        passwordRecovery.set(true);
      }
  
      if (session?.user) {
        await loadProfile();
      } else {
        clearProfile();
      }
  
    }
  );
}