<template>
    <div class="login">
        <img src="https://img01.sc115.com/uploads3/sc/jpgs/2007/apic26734_sc115.com.jpg" alt="">
        <div class="row justify-content-md-center">
            <div class="col-4">
                <form @submit.prevent="login">
                    <div class="mb-3">
                        <label for="username" class="form-label">用户名</label>
                        <input v-model="username" type="texdt" class="form-control" id="username">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">密码</label>
                        <input v-model="password" type="password" class="form-control" id="password">
                    </div>
                    <div class="error-message">{{ error_message }}</div>
                    <button type="submit" class="btn btn-primary login-btn">登录</button>
                    <a class="register-btn" href="/gigplatform/register/">注册</a>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';

export default {
    name: 'LoginView',
    components: {
    },
    setup() {
        const store = useStore();
        let username = ref('');
        let password = ref('');
        let error_message = ref('');

        const login = () => {
            error_message.value = '';
            store.dispatch("login", {
                username: username.value,
                password: password.value,
                success() {
                    router.push({ name: 'home', });
                },
                error() {
                    error_message.value = '用户名或密码错误';
                }
            })
        }

        return {
            username,
            password,
            error_message,
            login,
        }
    }
}
</script>

<style scoped>
.login-btn {
    width: 100%;
}

.register-btn {
    margin-top: 10px;
    float: right;
    cursor: pointer;
    text-decoration: none;
    color: black;
}

img {
    width: 100vw;
    height: 100vh;
}

.error-message {
    color: red;
}

.login {
    position: relative;
    display: inline-block;
}

.justify-content-md-center {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>