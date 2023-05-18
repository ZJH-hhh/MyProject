<template>
    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col-4 img-center">
                    <img class="img-fluid" :src="user.photo" alt="">
                </div>
                <div class="col-8">
                    <div class="username">{{ user.username }}</div>
                    <div class="fans">粉丝数：{{ user.followerCount }}</div>
                    <button @click="follow" v-if="!user.is_followed" type="button" class="btn btn-primary">+关注</button>
                    <button @click="unfollow" v-if="user.is_followed" type="button" class="btn btn-primary">取消关注</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import { computed } from 'vue'; // 用于计算
import $ from 'jquery';
import { useStore } from 'vuex';

export default {
    name: 'UserProfileInfo',
    props: { // 父组件传递的信息要放到props属性中
        user: {
            type: Object,
            required: true,
        },
    },
    setup(props, context) {
        const store = useStore();

        const follow = () => {
            $.ajax({
                url: 'https://app165.acapp.acwing.com.cn/myspace/follow/',
                type: 'POST',
                data: {
                    target_id: props.user.id
                },
                headers: {
                    'Authorization': 'Bearer ' + store.state.user.access,
                },
                success(response) {
                    if (response.result === 'success') {
                        context.emit('follow');
                    }
                }
            });
        }

        const unfollow = () => {
            $.ajax({
                url: 'https://app165.acapp.acwing.com.cn/myspace/follow/',
                type: 'POST',
                data: {
                    target_id: props.user.id
                },
                headers: {
                    'Authorization': 'Bearer ' + store.state.user.access,
                },
                success(response) {
                    if (response.result === 'success') {
                        context.emit('unfollow');
                    }
                }
            });
        }

        return {
            follow,
            unfollow,
        }
    },
}
</script>

<style scoped>
img {
    border-radius: 50%;
}

.username {
    font-size: 25px;
    font-weight: bolder;
}

.fans {
    font-size: 15px;
    margin-bottom: 2px;
}

.img-center {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
</style>