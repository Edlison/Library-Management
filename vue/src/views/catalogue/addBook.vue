<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item label="书名">
        <el-input v-model="form.name" />
      </el-form-item>
        <el-form-item label="作者">
        <el-input v-model="form.author" />
      </el-form-item>
      <el-form-item label="出版社">
        <el-input v-model="form.public" />
      </el-form-item>
      <el-form-item label="分类">
        <el-select v-model="form.class" placeholder="选择书的类别">
          <el-option label="小说" value="1" />
          <el-option label="随笔" value="2" />
          <el-option label="诗歌" value="3" />
          <el-option label="名著" value="4" />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Create</el-button>
        <el-button @click="onCancel">Cancel</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { addBook } from "@/api/addBook";
export default {
  data() {
    return {
      form: {
        name: '',
        author: '',
        public: '',
        class: '',
      }
    }
  },
  methods: {
    onSubmit() {
      console.log(this.form);
      if (this.form.name && this.form.author &&this.form.public &&this.form.class ) {
        var formData = this.form;
        addBook(formData).then((res) => {
          if (res == "add") {
            this.$message({
              message: "添加成功",
            });
          }else{
            this.$message({
          message: "出错，添加失败！",
          type: "warning",
        });  
          }
        });
      } else {
        this.$message({
          message: "信息不全！",
          type: "warning",
        });
      }
    },
    onCancel() {
        this.form='';
      this.$message({
        message: "cancel!",
        type: "warning",
      });
    },
  },
};
</script>

<style scoped>
.line{
  text-align: center;
}
</style>

