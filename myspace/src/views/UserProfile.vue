<template>
    <ContentBase>
        <div class="row">
            <div class="col-3">
                <UserProfileInfo @follow="follow" @unfollow="unfollow" :user="user" /> <!--将user传到子组件UserProfileInfo中-->
                <UserProfileWrite v-if="is_me" @post="post" />
            </div>
            <div class="col-9">
                <UserProfilePosts :user="user" :posts="posts" @delete_a_post="delete_a_post" />
            </div>
        </div>
    </ContentBase>
</template>
  
<script>
import ContentBase from '../components/ContentBase';
import UserProfileInfo from '../components/UserProfileInfo';
import UserProfilePosts from '../components/UserProfilePosts';
import UserProfileWrite from '../components/UserProfileWrite';
import { reactive } from 'vue';
import { useRoute } from 'vue-router';
import $ from 'jquery';
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
    name: 'UserProfile',
    components: { // 表示在template中会用到哪些其他的组件
        ContentBase,
        UserProfileInfo,
        UserProfilePosts,
        UserProfileWrite,
    },
    setup() {
        const store = useStore();
        const route = useRoute();
        const userid = parseInt(route.params.userid);
        const user = reactive({});
        const posts = reactive({});

        $.ajax({
            url: 'https://app165.acapp.acwing.com.cn/myspace/getinfo/',
            type: 'GET',
            data: {
                user_id: userid,
            },
            headers: {
                'Authorization': 'Bearer ' + store.state.user.access
            },
            success(response) {
                user.id = response.id;
                user.username = response.username;
                user.photo = response.photo;
                user.followerCount = response.followerCount;
                user.is_followed = response.is_followed;
            }
        });

        $.ajax({
            url: 'https://app165.acapp.acwing.com.cn/myspace/post/',
            type: 'GET',
            data: {
                user_id: userid,
            },
            headers: {
                'Authorization': 'Bearer ' + store.state.user.access
            },
            success(response) {
                posts.count = response.length;
                posts.posts = response;
            }
        });

        const follow = () => {
            user.is_followed = true;
            user.followerCount++;
        }

        const unfollow = () => {
            user.is_followed = false;
            user.followerCount--;
        }

        const post = content => {
            posts.count++;
            posts.posts.unshift({
                id: post.count,
                userid: 1,
                content: content,
            })
        }

        const delete_a_post = post_id => {
            posts.posts = posts.posts.filter(post => post.id !== post_id);
            posts.count = posts.posts.length;
        }

        const is_me = computed(() => userid === store.state.user.id);

        return {
            user,
            follow,
            unfollow,
            posts,
            post,
            is_me,
            delete_a_post,
        }
    },
}
</script>
  
<style scoped></style>
  