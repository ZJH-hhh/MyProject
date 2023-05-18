<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container">
            <router-link class="navbar-brand" :to="{ name: 'home' }">导航</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link class="nav-link active" aria-current="page" :to="{ name: 'home' }">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'LabelSpread' }">标签传播算法</router-link>
                    </li>
                    <!-- <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'SparkView' }">Spark实战</router-link>
                    </li> -->
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'NavBar',
}
</script>

<style scoped>
.navbar {
    background-color: rgb(249, 249, 249);
}
</style>