<script>
  export let data;
  
  const PREFIX = "http://localhost:5000/getq?";
  
  let sub, klas, chap,
  opt_open = true,
  current_q = null;
  
  function toggleOpt() {
    opt_open = !opt_open;
  }

  async function getQ() {
    const res = await fetch(PREFIX)
      .catch(e => console.error(res));
    
    current_q = res;
    return;
  }
</script>



<svelte:head>
  <title>JEE Test</title>
</svelte:head>



<section>
  <div class="titleBox">
    <h1> JEE Test Options </h1>
    
    <button on:click="{toggleOpt}">
      {#if opt_open }
      close
      {:else }
      open
      {/if }
    </button>
  </div>

  <div id="options" class:open={opt_open}>
    <form on:submit|preventDefault="{null}">
      <div>
        <label for="inklas">
          Class
        </label>
        <select id="inklas" bind:value="{klas}">
          <option value="2" selected>XI and XII</option>
          <option value="0">XI</option>
          <option value="1">XII</option>
        </select>
      </div>

      <div>
        <label for="insub">
          Subject
        </label>
        <select id="insub" bind:value="{sub}">
          <option value="3" selected>All</option>
          <option value="0">Physics</option>
          <option value="1">Chemistry</option>
          <option value="2">Maths</option>
        </select>
      </div>
      
      <div>
        <label for="inchap">
          Chapter
        </label>
        <select id="inchap" bind:value="{chap}" disabed={klas==2 ||sub==3}>
          <option value=""> Any </option>
          {#if klas && sub && klas != 2 && sub != 3}
          {#each data[`${klas}${sub}`] as t, i}
            <option value="{i}"> {t[0]} </option>
          {/each}
          {/if}
        </select>
      </div>
      
      <!--div>
        <label for="innum">
          Questions
        </label>
        <div>
          <span> {num} </span>
            <input id="innum" bind:value="{num}" type="range" min="1" max="30" />
        </div>
      </div>

      <div>
        <label for="intimer">
          Timed
        </label>
        <input id="intimer" bind:checked="{timed}" type="checkbox" />
      </div-->
  </form>
</div>

<div class="questionBox">
  <div>
    {#if current_q} {res}
    {:else} Press 'Next' for questions
    {/if}
  </div>
</div>

<button class="nextButton" on:click="{getQ}">
  Next Question
</button>

</section>



<style>
section {
padding: 2rem .25rem;
margin: auto;
}

@media (min-width: 776px) {
  section {
  max-width: 60vw;
  }
}

div.titleBox > * {
display: inline;
margin-right: 1rem;
}

#options {
overflow: hidden;
transform: translateY(-20%);
max-height: 0;
transition: all 250ms ease-out;
}
#options.open {
max-height: 100vh;
transform: translateY(0);
}

form {
padding: .5rem;
margin-top: 2rem;
display: flex;
flex-direction: column;
background: linear-gradient(to left top, #dad1d1, #ecedef);
border-top: 1px solid #000;
border-left: 1px solid #000;
border-radius: 10px;
}

form div {
margin: .5rem 0 .5rem 0;
display: grid;
grid-template-columns: 1fr 2fr;
}

form input {
width: 100% !important;
}
form select {
width: 100%;
}
form input:last-child {
width: min-content !important;
}

div.questionBox {
padding: 1rem;
margin-top: 2rem;
background: #00000011;
box-shadow: 2px 2px 5px rgba(0,0,0,.2)
}

button.nextButton {
margin-top: 1rem;
display: block;
margin-x: auto;
}

</style>