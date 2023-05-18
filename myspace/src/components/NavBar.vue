<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container">
            <!--router-link为 a 标签的升级版，也是超链接但是是在前端渲染，不会刷新浏览器 -->
            <!--a 标签的超链接地址参数是 href，router-link是 :to"{}" -->
            <router-link class="navbar-brand" :to="{ name: 'home' }">MySpace</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
                aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'home' }">首页</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'userlist' }">好友列表</router-link>
                    </li>
                    <li class="nav-item" v-if="$store.state.user.is_login">
                        <router-link class="nav-link"
                            :to="{ name: 'userprofile', params: { userid: $store.state.user.id } }">我的空间</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav" v-if="!$store.state.user.is_login">
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'login' }">登录</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" :to="{ name: 'register' }">注册</router-link>
                    </li>
                </ul>
                <ul class="navbar-nav" v-else>
                    <li class="nav-item">
                        <router-link class="nav-link"
                            :to="{ name: 'userprofile', params: { userid: $store.state.user.id } }">{{
                                $store.state.user.username }}</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" style="cursor: pointer;" @click="logout"
                            :to="{ name: 'home' }">退出</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import { useStore } from 'vuex';

export default {
    name: "NavBar",
    setup() {
        const store = useStore();

        const logout = () => {
            store.commit('logout');
        };

        return {
            logout,
        }
    }
}
</script>

<!--加上scoped可以使不同组件不相互影响-->
<style scoped>
.navbar {
    background-color: rgb(249, 249, 249);
}
</style>