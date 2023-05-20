<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container">
            <!--router-link为 a 标签的升级版，也是超链接但是是在前端渲染，不会刷新浏览器 -->
            <!--a 标签的超链接地址参数是 href，router-link是 :to"{}" -->
            <a class="navbar-brand" href="">零工平台</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
                aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link" href="/gigplatform/" :to="{ name: 'home' }">首页</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'jobs', params: { 'jobname': 'all' } }">职位</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="">发布工作</a>
                    </li>
                </ul>
                <ul class="navbar-nav" v-if="!$store.state.user.is_login">
                    <li class="nav-item">
                        <router-link class="nav-link" href="/gigplatform/login/" :to="{ name: 'login' }">登录</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" href="/gigplatform/register/"
                            :to="{ name: 'register' }">注册</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav" v-else>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'login' }">{{ $store.state.user.username }}</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="">退出</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQD9rmAEnU3b7upruW8FhHd0t30qbsIPZkzCJV33fH45iTQE_BOoxyl7MMnwB4SE2SsyoA&usqp=CAU"
        alt=""> -->
</template>

<script>
import { useStore } from 'vuex';

export default {
    name: "NavBar",
    setup() {
        const store = useStore();

        return {
            store,
        }
    }
}
</script>

<!--加上scoped可以使不同组件不相互影响-->
<style scoped>
.navbar {
    background: linear-gradient(to right, cyan, 70%, rgb(59, 162, 123));
}

.navbar>a {
    cursor: pointer;
}
</style>