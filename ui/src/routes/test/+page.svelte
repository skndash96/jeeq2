<script>
  let num = 5,
      sub, klas,
      timed = false;
  
  function handleSubmit() {
    console.log(num, sub, klas, timed);
  }
</script>

<svelte:head>
	<title>JEE Test</title>
</svelte:head>

<section>
	<h1> JEE Test Options </h1>
	
	<form on:submit|preventDefault="{handleSubmit}">
	  <div>
	    <label> Class </label>
	    <select bind:value="{klas}">
	      <option value="2" selected>XI and XII</option>
	      <option value="0">XI</option>
	      <option value="1">XII</option>
	    </select>
	  </div>
	  
	  <div>
	    <label> Subject </label>
	    <select bind:value="{sub}">
	      <option value="3" selected>All</option>
	      <option value="0">Physics</option>
	      <option value="1">Chemistry</option>
	      <option value="2">Maths</option>
	    </select>
	  </div>
	  
	  <div>
	    <label> Questions </label>
	    <div>
	      <span> {num} </span>
	      <input bind:value="{num}" type="range" min="1" max="30"/>
	     </div>
	  </div>
	  
	  <div>
	    <label> Timed </label>
	    <input bind:checked="{timed}" type="checkbox" />
	  </div>
	  
	  <button type="submit">
	    Start Test
	  </button>
	</form>
</section>

<style>
  section {
    padding: 2rem .25rem;
  }
  
  h1 {
    font-size: var(--size-lg);
  }
  
  form {
    padding: .5rem;
    margin-top: 2rem;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    background: linear-gradient(to left top, #dad1d1, #ecedef);
    box-shadow: 5px 5px 10px rgba(0,0,0,.2);
    border: 1px solid #000;
    border-bottom: none;
    border-right: none;
  }
  
  form div {
    margin: .5rem 0 .5rem 0;
    display: grid;
    grid-template-columns: 1fr 2fr;
  }
  
  form input {
    width: 100% !important;
  }
  
  form button {
    margin: 1rem auto 0 auto;
    padding: .25rem .5rem;
  }
  
</style>
