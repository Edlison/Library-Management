<template>
  <div class="app-container">
    <el-card class="box-card">
      <div>
        {{ text }}
      </div>
    </el-card>
    <el-form ref="form" :model="form" label-width="120px" :rules="rule">
      <el-form-item label="书名" prop="name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="作者" prop="author">
        <el-input v-model="form.author" />
      </el-form-item>
      <el-form-item label="出版社" prop="public">
        <el-input v-model="form.public" />
      </el-form-item>
      <el-form-item label="ISBN" prop="isbn">
        <el-input v-model="form.isbn" />
      <div style="margin-top: 10px">示例：978-7-115-47066-9，必须使用 -（英文字符）进行分隔</div>
        <!-- <el-select
          v-model="form.isbn1"
          placeholder="选择第一段"
          style="margin-right: 10px"
        >
          <el-option label="978" value="978" />
          <el-option label="979" value="979" />
        </el-select>
        <span>——</span>
        <div style="display: inline-block; margin: 0 10px">
          <el-input
            placeholder="第二段（1-5位数字）"
            v-model="form.isbn2"
            ref="recond"
          >
          </el-input>
        </div>
        <span>——</span>
        <div style="display: inline-block; margin: 0 10px">
          <el-input placeholder="第三段（2-5位数字）" v-model="form.isbn3" ref="thrid">
          </el-input>
        </div>
        <span>——</span>
        <div style="margin-top: 10px">
          <div style="display: inline-block; margin-right: 10px" ref="fouth">
            <el-input placeholder="第四段（1-6位数字）" v-model="form.isbn4">
            </el-input>
          </div>
          <span>——</span>
          <div style="display: inline-block; margin: 0 10px" ref="fifth">
            <el-input placeholder="第五段（1位数字）" v-model="form.isbn5">
            </el-input>
          </div>
        </div> -->
      </el-form-item>
      <el-form-item label="单价">
        <el-input v-model="form.price" />
      </el-form-item>
      <el-form-item label="数量">
        <el-input v-model="form.number" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button @click="onCancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<style scope>
.el-card {
  text-align: center;
  margin: 0 auto 10px auto;
}
.el-select .el-input {
  width: 191px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>
<script>
import { addBook } from "@/api/addBook";
export default {
  data() {
    return {
      text: "在此输入您希望图书馆购入的书籍信息",
      form: {
        name: "",
        author: "",
        public: "",
        class: "",
        price: "",
        isbn:[],
        number: "",
      },
      rule: {
        name: [
          { required: true, message: "请输入书名", trigger: "blur" },
          // { min: 1, max: 50, message: '长度在 1 到 50 个字符', trigger: 'blur' }
        ],
        author: [{ required: true, message: "请输入作者", trigger: "blur" }],
        public: [{ required: true, message: "请输入出版社", trigger: "blur" }],
        isbn: [{ required: true, message: "请输入ISBN ", trigger: "blur" },
        {pattern: /^((978|979)-)?([0-9]{1,5}-[0-9]{1,6}-[0-9]{1,5}-([0-9]|X))$/, message: 'ISBN格式有误'}],
      },
    };
  },
  
  methods: {
    onSubmit() {
      console.log(JSON.stringify(this.form));
      // if (
      //   this.form.name &&
      //   this.form.author &&
      //   this.form.public &&
      //   this.form.class
      // ) {
      //   var formData = this.form;
      //   addBook(formData).then((res) => {
      //     if (res == "add") {
      //       this.$message({
      //         message: "添加成功",
      //       });
      //     } else {
      //       this.$message({
      //         message: "出错，添加失败！",
      //         type: "warning",
      //       });
      //     }
      //   });
      // } else {
      //   this.$message({
      //     message: "信息不全！",
      //     type: "warning",
      //   });
      // }
    },
    onCancel() {
      this.form = "";
      this.$message({
        message: "取消!",
        type: "warning",
      });
    },

  },
};

</script>



