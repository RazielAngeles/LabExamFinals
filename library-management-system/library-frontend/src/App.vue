<template>
  <div>
    <nav>
      <ul>
        <li><router-link to="/">Books</router-link></li>
        <li><router-link to="/borrow">Borrow</router-link></li>
        <li><router-link to="/return">Return</router-link></li>
        <li><router-link to="/transactions">Transactions</router-link></li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>