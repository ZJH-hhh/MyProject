<template>
    <NavBar />
    <div class="postjob">
        <ContentBase>
            <div class="input-list">
                <div class="headline">
                    发布基本信息
                </div>
                <div class="subline">
                    打*为必填
                </div>
                <form @submit.prevent="postjob">
                    <div class="mb-3">
                        <label for="jobname" class="form-label"><span class="highlight">*</span>工作名称</label>
                        <input v-model="jobname" type="text" class="form-control" id="jobname" required>
                    </div>
                    <div class="mb-3">
                        <label for="address" class="form-label"><span class="highlight">*</span>工作地点</label>
                        <input v-model="address" type="text" class="form-control" id="address" required>
                    </div>
                    <div class="mb-3">
                        <label for="content" class="form-label"><span class="highlight">*</span>工作内容</label>
                        <input v-model="content" type="text" class="form-control" id="content" required>
                    </div>
                    <div class="mb-3">
                        <label for="require" class="form-label"><span class="highlight">*</span>具体要求</label>
                        <input v-model="require" type="text" class="form-control" id="require" required>
                    </div>
                    <div class="mb-3">
                        <label for="tag" class="form-label">标签</label>
                        <input v-model="tag" type="text" class="form-control" id="tag">
                    </div>
                    <div class="mb-3">
                        <label for="kind" class="form-label">分类</label>
                        <input v-model="kind" type="text" class="form-control" id="kind">
                    </div>
                    <div class="mb-3">
                        <label for="wage" class="form-label"><span class="highlight">*</span>工资</label>
                        <input v-model="wage" type="text" class="form-control" id="wage" required>
                    </div>
                    <div class="mb-3">
                        <label for="experience" class="form-label">经验要求</label>
                        <input v-model="experience" type="text" class="form-control" id="experience">
                    </div>
                    <div class="mb-3">
                        <label for="academic" class="form-label">学历要求</label>
                        <input v-model="academic" type="text" class="form-control" id="academic">
                    </div>
                    <div class="mb-3">
                        <label for="tele" class="form-label"><span class="highlight">*</span>联系方式</label>
                        <input v-model="tele" type="number" class="form-control" id="tele" required>
                    </div>
                    <!-- <button type="submit" class="btn btn-primary">发布</button> -->
                    <button type="submit" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                        发布
                    </button>
                </form>
            </div>

            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" id="exampleModalLabel">提示</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            工作发布成功
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">关闭</button>
                            <button type="button" class="btn btn-primary">确定</button>
                        </div>
                    </div>
                </div>
            </div>
        </ContentBase>
    </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import ContentBase from '@/components/ContentBase.vue';
import { ref } from 'vue';
import $ from 'jquery';
// import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

export default {
    name: 'PostJob',
    components: {
        NavBar,
        ContentBase,
    },
    setup() {
        // const router = useRouter();
        const store = useStore();

        let jobname = ref('');
        let address = ref('');
        let content = ref('');
        let require = ref('');
        let tag = ref('');
        let wage = ref('');
        let experience = ref('');
        let academic = ref('');
        let tele = ref('');
        let kind = ref('');

        const postjob = () => {
            $.ajax({
                url: 'http://127.0.0.1:8000/api/jobs/',
                type: 'POST',
                data: {
                    name: jobname.value,
                    address: address.value,
                    employer: store.state.user.username,
                    content: content.value,
                    require: require.value,
                    tag: tag.value,
                    wage: wage.value,
                    experience: experience.value,
                    academic: academic.value,
                    kind: kind.value,
                },
                success: response => {
                    console.log(response);
                    // router.push({ name: 'jobs', params: { jobname: 'all' } });
                }
            })
        }

        return {
            jobname,
            address,
            content,
            require,
            tag,
            wage,
            experience,
            academic,
            tele,
            kind,
            postjob,
        }
    }
}
</script>

<style scoped>
.postjob {
    /* height: 100vh; */
    background-color: #E4F3F5;
}

.input-list {
    height: 100vh;
    margin-left: 150px;
    margin-right: 150px;
    overflow: auto;
}

.headline {
    width: 20%;
    font-size: 30px;
    color: #1FCEB9;
}

.subline {
    color: #666;
}

.headline,
.subline {
    display: inline-block;
}

.highlight {
    color: red;
}
</style>