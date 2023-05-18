<template>
    <ContentBase>
        <div class="card friend" v-for="friend in friends" :key="friend.id" @click="open_user_profile(friend.id)">
            <div class="card-body">
                <div class="row">
                    <div class="col-1">
                        <img class="img-fluid" :src="friend.photo" alt="">
                    </div>
                    <div class="col-11">
                        <div class="username">{{ friend.username }}</div>
                        <div class="followerCount">{{ friend.followerCount }}</div>
                    </div>
                </div>
            </div>
        </div>
    </ContentBase>
</template>
  
<script>

import ContentBase from '../components/ContentBase';
import $ from 'jquery';
import { ref } from 'vue';
import router from '@/router/index';
import { useStore } from 'vuex';

export default {
    name: 'UserList',
    components: { // 表示在template中会用到哪些其他的组件
        ContentBase,
    },
    setup() {
        const store = useStore();
        let friends = ref([]);

        $.ajax({
            url: 'https://app165.acapp.acwing.com.cn/myspace/userlist/',
            type: 'get',
            success(response) {
                friends.value = response;
            }
        });

        const open_user_profile = (userid) => {
            if (store.state.user.is_login) {
                console.log(userid);
                router.push({
                    name: 'userprofile',
                    params: {
                        userid: userid
                    }
                });
            } else {
                router.push({
                    name: 'login',
                });
            }
        }

        return {
            friends,
            open_user_profile,
        };
    }
}
</script>
  
<style scoped>
.friend {
    margin-bottom: 10px;
}

img {
    border-radius: 50%;
    cursor: pointer;
}

.username {
    font-weight: bolder;
    height: 50%;
    cursor: pointer;
}

.followerCount {
    font-size: 12px;
    height: 50%;
    color: gray;
}

img:hover {
    transform: scale(1.1);
    transition: 200ms;
    box-shadow: 2px 2px 10px;
}
</style>
  