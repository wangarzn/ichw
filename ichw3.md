* 高速缓冲存储器是存在于主存与CPU之间的一级存储器， 由静态存储芯片(SRAM)组成，容量比较小但速度比主存高得多， 接近于CPU的速度。
  主要由三大部分组成：Cache存储体，地址转换部件，替换部件。cache的结构包含地址和内容，cache的内容除了存的数据（data）之外，
  还包含存的数据的物理内存的地址信息（tag），因为CPU发出的寻址信息都是针对物理内存发出的，所以cache中除了要保存数据信息之外，还要保存数据对应的地址，
  这样才能在cache中根据物理内存的地址信息查找物理内存中对应的数据。（当然为了加快寻找速度，cache中一般还包含一个有效位（valid），
  用来标记这个cache line是否保存着有效的数据）。一个tag和它对应的数据组成的一行称为一个cache line。

* 寄存器和内存之间读写速度的差距是很大的，而内存和磁盘之间的读写速度差距也很大。
  在两端插入一个高速缓存存储器，可以帮忙存储内存要传的数据，然后再把这些数据传给寄存器，这样就提高了速度。
  如果没有cache，CPU每次都要去较庞大内存中找需要的数据，读取速度很慢，读取的数据会被很快的运算完，造成时间上的浪费。
  加入cache后，cache可以提前从内存中读取数据，暂时存储，因为cache容量比较小，所以CPU读取cache中的数据时比前者快很多，因此提高了时间利用率。
  像这种理想的CPU要运算的数据在cache中有的，称为**缓存命中** 。倘若CPU要运算的数据在cache中没有，称为**缓存不命中** 。
  若发生了缓存不命中，会把该数据缓存在第k层中，如果当前有空余的空间还好，可以直接缓存，但是如果没有空间就会导致替换的发生（即覆盖第k层中的某一个块）。
  