# 第5章 CSS

> 一种现代的、模块化的方法,详看第4章

1. 从OOCSS方法：

   - 分离容器和内容，不再使用位置作为样式的限定词 ==> 不允许出现top、left、right、bottom等词汇。

2. SMACSS方法:

   - 分离颗粒度：基础、布局、模块、状态、主题 ==> 将布局和模块分离到不同的文件夹，不允许布局代码出现在sass的代码中

3. BEM

   - 给每个CSS类名一个独一无二的标识 

   ```html
   <body>
     <div class="main">
       <h2 class="content__title">Header</h2>
     </div>
     <div class="sidebar">
       <h2 class="content__title--reversed">Sidebar</h2>
     </div>
     <div class="calender">
       <h2 class="calender__title">calender</h2>
     </div>
   </body>
   <style>
   /**模块文件夹 **/
   .content__title{
     font-size: 24px;
     color:red
   }
   .content__title--reversed{
     font-size: 20px;
     background: red;
     color: white;
   }
   .calender_title{6666
     font-size: 20px;
     color: red;
   }
   
   /** 布局文件夹 **/
   .main{
     float: left;
   }
   .sidebar{
     float: right;
   }
   </style>6666
   ```

   ## 原则

   1. 单一职责原则

      - 所有的样式应该为单一目的而创建，并且能够很好的实现这个目标。==> 会造成代码重复，但是其可持续性大大大于代码重复本身。再加上现在的压缩技术，代码重复可以忽略不计数。
      - 关注样式应用的内容，而非样式本身 ==> 不设置padding-10、font-size-20和color-green类似的样式

      非单一职责引发的问题： 优先级、位置依赖、多重继承、深度嵌套、颜色重置。

   ```html
   <!-- 虽然都为title,但是不一定一直保持红色，我们不应该整合两段代码 -->
   <body>
     <div class="blog">
       <h2 class="blog_title">Header</h2>
     </div>
     <div class="calender">
       <h2 class="calender__title">calender</h2>
     </div>
   </body>
   <style>
   /**模块文件夹 **/
   .content__title{
     font-size: 24px;
     color:red
   }
   .calender__title{
     font-size: 20px;
     background: red;
     color: white;
   }
   
   </style>
   ```

   2. 单一样式来源	

   - 分离与父类相关的，和与父类无关的，减少对父类的依赖
   - 注意样式的位置

   ```html
   <body>
     <main class="content">
       <div class="blog">
         <h2 class="blog_title">Header</h2>
       </div>
       <div class="calender">
         <h2 class="calender__title">calender</h2>
       </div>
     </main>
   </body>
   <style>
     .blog__title {
       font-size: 24px;
       color: red;
     }
     .content .blog__title{
       font-size:20px;
     }
     .calender__title {
       font-size: 20px;
       background: red;
       color: white;
     }
   </style>
   
   ```

   3. 组件修饰符

      > 当上下文依赖十分严重时，采用组件修饰符

      ```html
      <body>
        <main class="content">
          <div class="blog">
            <h2 class="blog_title">Header</h2>
          </div>
          <div class="calender calender__nested">
            <h2 class="calender__title">calender</h2>
          </div>
        </main>
      </body>
      <style>
        .blog__title {
          font-size: 24px;
          color: red;
        }
        .content .blog__title{
          font-size:20px;
        }
        .calender__title {
          font-size: 20px;
          background: red;
          color: white;
        }
        .calender__nested .calender__title{
          font-size:16px;
        }
      </style>
      
      ```

      