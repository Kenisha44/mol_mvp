import { writable } from 'svelte/store';

import { supabase } from '../lib/supabaseClient.js';


export const profile = writable(null);

export const profileLoading = writable(true);

export const profileError = writable('');


export async function loadProfile() {
  profileLoading.set(true);
  profileError.set('');

  try {
    const {
      data: { user },
      error: userError
    } = await supabase.auth.getUser();


    if (userError) {
      throw userError;
    }


    if (!user) {
      profile.set(null);
      return null;
    }


    const {
      data,
      error
    } = await supabase
      .from('profiles')
      .select(`
        id,
        plan,
        analysis_count,
        export_count,
        usage_period_start,
        created_at,
        updated_at
      `)
      .eq('id', user.id)
      .single();


    if (error) {
      throw error;
    }


    profile.set(data);

    return data;

  } catch (error) {

    console.error(
      'Unable to load MOL profile:',
      error
    );

    profile.set(null);

    profileError.set(
      error?.message ||
      'Unable to load account profile.'
    );

    return null;

  } finally {

    profileLoading.set(false);

  }
}


export function clearProfile() {
  profile.set(null);
  profileError.set('');
  profileLoading.set(false);
}