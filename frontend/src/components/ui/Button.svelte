<script>
  export let text = '';
  export let variant = 'primary';
  export let disabled = false;
  export let type = 'button';
  export let onClick = () => {};
</script>

<button
  class:primary={variant === 'primary'}
  class:secondary={variant === 'secondary'}
  class:mini={variant === 'mini'}
  {type}
  {disabled}
  on:click={onClick}
>
  <slot>{text}</slot>
</button>