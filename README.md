# XX1 CINEMA - Sistem Manajemen Film Python

## 1. Deskripsi Singkat Program

XX1 Cinema merupakan program berbasis Python yang digunakan untuk
melakukan pengelolaan data film sederhana dengan sistem login dan
pembagian hak akses pengguna.

Program memiliki dua role pengguna:

-   **Admin**: dapat melihat, menambah, mengubah, dan menghapus data
    film.
-   **User**: hanya dapat melihat daftar film.

Program menerapkan konsep pemrograman Python seperti function, list,
dictionary, percabangan, perulangan, exception handling, dan CRUD.

------------------------------------------------------------------------

# 2. Flowchart Program

Flowchart program dapat dilihat pada file berikut:<mxfile host="app.diagrams.net">
  <diagram id="xx1-cinema" name="Flowchart XX1 Cinema">
    <mxGraphModel dx="8893" dy="3307" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="6387" pageHeight="4965" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="start" parent="1" style="ellipse;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="MULAI" vertex="1">
          <mxGeometry height="70" width="300" x="950" y="60" as="geometry" />
        </mxCell>
        <mxCell id="lh" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan&#xa;&quot;LOGIN XX1 CINEMA&quot;" vertex="1">
          <mxGeometry height="104" width="440" x="880" y="688" as="geometry" />
        </mxCell>
        <mxCell id="us" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input username" vertex="1">
          <mxGeometry height="85" width="440" x="880" y="930" as="geometry" />
        </mxCell>
        <mxCell id="pw" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input password" vertex="1">
          <mxGeometry height="85" width="440" x="880" y="1210" as="geometry" />
        </mxCell>
        <mxCell id="dc" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Username dan password&#xa;benar?" vertex="1">
          <mxGeometry height="156" width="469" x="865.5" y="1440" as="geometry" />
        </mxCell>
        <mxCell id="lb" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan &quot;Login berhasil&quot;&#xa;dan tanggal jam" vertex="1">
          <mxGeometry height="104" width="462" x="869" y="1703" as="geometry" />
        </mxCell>
        <mxCell id="n3" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Role admin?" vertex="1">
          <mxGeometry height="145" width="380" x="910" y="1990" as="geometry" />
        </mxCell>
        <mxCell id="n3a" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan&#xa;1. Lihat film&#xa;2. Tambah Film&#xa;3. Ubah Film&#xa;4. Hapus Film&#xa;5. Logout" vertex="1">
          <mxGeometry height="164" width="440" x="880" y="2230" as="geometry" />
        </mxCell>
        <mxCell id="n5" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input pilih menu" vertex="1">
          <mxGeometry height="85" width="440" x="880" y="2540" as="geometry" />
        </mxCell>
        <mxCell id="gl" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan &quot;Login gagal&quot;" vertex="1">
          <mxGeometry height="85" width="440" x="1670" y="930" as="geometry" />
        </mxCell>
        <mxCell id="sel" parent="1" style="ellipse;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="SELESAI" vertex="1">
          <mxGeometry height="70" width="300" x="1740" y="1167" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-10" edge="1" parent="1" source="ls" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" target="lh">
          <mxGeometry relative="1" x="-0.1083" as="geometry">
            <Array as="points">
              <mxPoint x="2330" y="1518" />
              <mxPoint x="2330" y="740" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ls" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan &quot;Login salah&quot;" vertex="1">
          <mxGeometry height="85" width="440" x="1660" y="1475.5" as="geometry" />
        </mxCell>
        <mxCell id="d1" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="pilih = 1 ?" vertex="1">
          <mxGeometry height="145" width="380" x="910" y="2780" as="geometry" />
        </mxCell>
        <mxCell id="d2" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="pilih = 2 dan&#xa;role admin?" vertex="1">
          <mxGeometry height="156" width="380" x="910" y="3041" as="geometry" />
        </mxCell>
        <mxCell id="d3" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="pilih = 3 dan&#xa;role admin?" vertex="1">
          <mxGeometry height="156" width="380" x="910" y="3267" as="geometry" />
        </mxCell>
        <mxCell id="d4" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="pilih = 4 dan&#xa;role admin?" vertex="1">
          <mxGeometry height="156" width="380" x="910" y="3493" as="geometry" />
        </mxCell>
        <mxCell id="d5" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="pilih = 5 ?" vertex="1">
          <mxGeometry height="145" width="380" x="910" y="3719" as="geometry" />
        </mxCell>
        <mxCell id="bad" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan&#xa;&quot;Menu tidak tersedia&quot;" vertex="1">
          <mxGeometry height="104" width="440" x="880" y="3934" as="geometry" />
        </mxCell>
        <mxCell id="lo" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan &quot;Logout berhasil&quot;" vertex="1">
          <mxGeometry height="85" width="474" x="383" y="3749" as="geometry" />
        </mxCell>
        <mxCell id="h0" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan daftar film" vertex="1">
          <mxGeometry height="85" width="440" x="1980" y="3631" as="geometry" />
        </mxCell>
        <mxCell id="h1" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input nomor film" vertex="1">
          <mxGeometry height="85" width="440" x="1980" y="3771" as="geometry" />
        </mxCell>
        <mxCell id="h2" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Nomor berupa angka?" vertex="1">
          <mxGeometry height="145" width="431" x="1984.5" y="3911" as="geometry" />
        </mxCell>
        <mxCell id="h2m" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input tidak valid" vertex="1">
          <mxGeometry height="85" width="440" x="2600" y="3941" as="geometry" />
        </mxCell>
        <mxCell id="h3" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Nomor ada di daftar?" vertex="1">
          <mxGeometry height="145" width="450" x="1975" y="4111" as="geometry" />
        </mxCell>
        <mxCell id="h3m" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Film tidak ditemukan" vertex="1">
          <mxGeometry height="85" width="440" x="2600" y="4141" as="geometry" />
        </mxCell>
        <mxCell id="h4" parent="1" style="rounded=0;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Hapus film dari daftar" vertex="1">
          <mxGeometry height="80" width="440" x="1980" y="4311" as="geometry" />
        </mxCell>
        <mxCell id="h5" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan&#xa;&quot;Film berhasil dihapus&quot;" vertex="1">
          <mxGeometry height="104" width="440" x="1980" y="4446" as="geometry" />
        </mxCell>
        <mxCell id="u0" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan daftar film" vertex="1">
          <mxGeometry height="85" width="440" x="3230" y="3405" as="geometry" />
        </mxCell>
        <mxCell id="u1" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input nomor film" vertex="1">
          <mxGeometry height="85" width="440" x="3230" y="3545" as="geometry" />
        </mxCell>
        <mxCell id="u2" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Nomor berupa angka?" vertex="1">
          <mxGeometry height="145" width="431" x="3234.5" y="3685" as="geometry" />
        </mxCell>
        <mxCell id="u2m" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input tidak valid" vertex="1">
          <mxGeometry height="85" width="440" x="3850" y="3715" as="geometry" />
        </mxCell>
        <mxCell id="u3" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Nomor ada di daftar?" vertex="1">
          <mxGeometry height="145" width="450" x="3225" y="3885" as="geometry" />
        </mxCell>
        <mxCell id="u3m" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Film tidak ditemukan" vertex="1">
          <mxGeometry height="85" width="440" x="3850" y="3915" as="geometry" />
        </mxCell>
        <mxCell id="u4" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input nama, kategori,&#xa;harga baru" vertex="1">
          <mxGeometry height="104" width="440" x="3230" y="4085" as="geometry" />
        </mxCell>
        <mxCell id="u5" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Harga berupa angka?" vertex="1">
          <mxGeometry height="145" width="431" x="3234.5" y="4244" as="geometry" />
        </mxCell>
        <mxCell id="u5m" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input tidak valid" vertex="1">
          <mxGeometry height="85" width="440" x="3850" y="4274" as="geometry" />
        </mxCell>
        <mxCell id="u6" parent="1" style="rounded=0;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Ganti data film" vertex="1">
          <mxGeometry height="80" width="440" x="3230" y="4444" as="geometry" />
        </mxCell>
        <mxCell id="u7" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan&#xa;&quot;Film berhasil diubah&quot;" vertex="1">
          <mxGeometry height="104" width="440" x="3230" y="4579" as="geometry" />
        </mxCell>
        <mxCell id="t0" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input nama film,&#xa;kategori, harga" vertex="1">
          <mxGeometry height="104" width="440" x="4480" y="3179" as="geometry" />
        </mxCell>
        <mxCell id="t1" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Harga berupa angka?" vertex="1">
          <mxGeometry height="145" width="431" x="4484.5" y="3338" as="geometry" />
        </mxCell>
        <mxCell id="t1m" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Input harga harus angka" vertex="1">
          <mxGeometry height="85" width="440" x="5100" y="3368" as="geometry" />
        </mxCell>
        <mxCell id="t2" parent="1" style="rounded=0;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tambah film ke daftar" vertex="1">
          <mxGeometry height="80" width="440" x="4480" y="3538" as="geometry" />
        </mxCell>
        <mxCell id="t3" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan &quot;Film berhasil ditambah&quot;&#xa;dan kode acak" vertex="1">
          <mxGeometry height="104" width="558" x="4421" y="3673" as="geometry" />
        </mxCell>
        <mxCell id="v0" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan daftar film&#xa;(no, nama, kategori, harga)" vertex="1">
          <mxGeometry height="104" width="474" x="5713" y="2950" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-12" edge="1" parent="1" source="ent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="n3">
          <mxGeometry relative="1" x="-0.1824" as="geometry">
            <Array as="points">
              <mxPoint x="530" y="4773" />
              <mxPoint x="530" y="2062.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ent" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tekan Enter untuk lanjut" vertex="1">
          <mxGeometry height="85" width="440" x="880" y="4730.5" as="geometry" />
        </mxCell>
        <mxCell id="edge1" edge="1" parent="1" source="start" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="lh" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1100" y="190" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="edge5" edge="1" parent="1" source="lh" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="us" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1100" y="852" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="edge8" edge="1" parent="1" source="us" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;entryX=0;entryY=0.5;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" target="gl" value="Tidak">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1290" y="1064.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="edge9" edge="1" parent="1" source="gl" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="sel" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge10" edge="1" parent="1" source="us" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="pw" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge11" edge="1" parent="1" source="pw" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="dc" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge12" edge="1" parent="1" source="dc" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="lb" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge13" edge="1" parent="1" source="dc" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" target="ls" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge16" edge="1" parent="1" source="lb" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="n3" value="">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1100" y="1867" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="edge20" edge="1" parent="1" source="n3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;exitDx=0;exitDy=0;entryDx=0;entryDy=0;" target="n3a" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge22" edge="1" parent="1" source="n3a" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" target="n5" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points" />
            <mxPoint x="1100" y="2526" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="edge24" edge="1" parent="1" source="n5" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="d1" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge25" edge="1" parent="1" source="d1" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="d2" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge26" edge="1" parent="1" source="d2" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="d3" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge27" edge="1" parent="1" source="d3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="d4" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge28" edge="1" parent="1" source="d4" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="d5" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge29" edge="1" parent="1" source="d5" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="bad" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge30" edge="1" parent="1" source="d5" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0;exitY=0.5;entryX=1;entryY=0.5;" target="lo" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge31" edge="1" parent="1" source="lo" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0;exitY=0.5;entryX=0;entryY=0.5;" target="lh" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="180" y="3791.5" />
              <mxPoint x="180" y="740" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge32" edge="1" parent="1" source="d4" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0.5;entryY=0;" target="h0" value="Ya">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="2200" y="3571" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge33" edge="1" parent="1" source="h0" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="h1" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge34" edge="1" parent="1" source="h1" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="h2" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge35" edge="1" parent="1" source="h2" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" target="h2m" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge36" edge="1" parent="1" source="h2" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="h3" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge37" edge="1" parent="1" source="h3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" target="h3m" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge38" edge="1" parent="1" source="h3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="h4" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge39" edge="1" parent="1" source="h4" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="h5" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge40" edge="1" parent="1" source="d3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0.5;entryY=0;" target="u0" value="Ya">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="3450" y="3345" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge41" edge="1" parent="1" source="u0" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="u1" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge42" edge="1" parent="1" source="u1" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="u2" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge43" edge="1" parent="1" source="u2" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" target="u2m" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge44" edge="1" parent="1" source="u2" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="u3" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge45" edge="1" parent="1" source="u3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" target="u3m" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge46" edge="1" parent="1" source="u3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="u4" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge47" edge="1" parent="1" source="u4" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="u5" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge48" edge="1" parent="1" source="u5" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" target="u5m" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge49" edge="1" parent="1" source="u5" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="u6" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge50" edge="1" parent="1" source="u6" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="u7" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge51" edge="1" parent="1" source="d2" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0.5;entryY=0;" target="t0" value="Ya">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="4700" y="3119" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge52" edge="1" parent="1" source="t0" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="t1" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge53" edge="1" parent="1" source="t1" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0;entryY=0.5;" target="t1m" value="Tidak">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge54" edge="1" parent="1" source="t1" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="t2" value="Ya">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge55" edge="1" parent="1" source="t2" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="t3" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge56" edge="1" parent="1" source="d1" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0.5;entryY=0;" target="v0" value="Ya">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="5950" y="2852.5" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge57" edge="1" parent="1" source="bad" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" target="ent" value="">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="edge58" edge="1" parent="1" source="h5" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="2200" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge59" edge="1" parent="1" source="u7" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="3450" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge60" edge="1" parent="1" source="t3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="4700" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge61" edge="1" parent="1" source="v0" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=0.5;exitY=1;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="5950" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge62" edge="1" parent="1" source="h2m" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="3100" y="3983.5" />
              <mxPoint x="3100" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge63" edge="1" parent="1" source="h3m" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="3100" y="4183.5" />
              <mxPoint x="3100" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge64" edge="1" parent="1" source="u2m" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="4350" y="3757.5" />
              <mxPoint x="4350" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge65" edge="1" parent="1" source="u3m" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="4350" y="3957.5" />
              <mxPoint x="4350" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge66" edge="1" parent="1" source="u5m" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="4350" y="4316.5" />
              <mxPoint x="4350" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="edge67" edge="1" parent="1" source="t1m" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=1;entryY=0.5;" target="ent" value="">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="5600" y="3410.5" />
              <mxPoint x="5600" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-1" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Role user?" vertex="1">
          <mxGeometry height="145" width="380" x="1600" y="1990" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-17" edge="1" parent="1" source="9KKj1zGvKfXcdMq3ckd5-4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" target="9KKj1zGvKfXcdMq3ckd5-19">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="2470" y="2312" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-4" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan 1. lihat film&#xa;Tampilkan 5. Logout" vertex="1">
          <mxGeometry height="85" width="440" x="1840" y="2269.5" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-5" edge="1" parent="1" source="9KKj1zGvKfXcdMq3ckd5-1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.596;entryY=0.029;entryDx=0;entryDy=0;entryPerimeter=0;" target="9KKj1zGvKfXcdMq3ckd5-4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-7" connectable="0" parent="9KKj1zGvKfXcdMq3ckd5-5" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="YA" vertex="1">
          <mxGeometry relative="1" x="-0.3504" y="2" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-6" edge="1" parent="1" source="n3" style="edgeStyle=none;rounded=0;html=0;endArrow=block;endFill=1;strokeColor=#202020;strokeWidth=2;jumpStyle=arc;jumpSize=10;fontFamily=Arial;fontSize=18;labelBackgroundColor=#FFFFFF;exitX=1;exitY=0.5;entryX=0;entryY=0.5;exitDx=0;exitDy=0;entryDx=0;entryDy=0;" target="9KKj1zGvKfXcdMq3ckd5-1" value="">
          <mxGeometry relative="1" x="0.9795" as="geometry">
            <Array as="points" />
            <mxPoint x="1794" y="2360" as="sourcePoint" />
            <mxPoint x="1660" y="2360" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-11" connectable="0" parent="9KKj1zGvKfXcdMq3ckd5-6" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" value="TIDAK" vertex="1">
          <mxGeometry relative="1" x="0.011" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-24" edge="1" parent="1" source="9KKj1zGvKfXcdMq3ckd5-19" style="rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.75;entryDx=0;entryDy=0;" target="9KKj1zGvKfXcdMq3ckd5-23">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-29" edge="1" parent="1" source="9KKj1zGvKfXcdMq3ckd5-19" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" target="9KKj1zGvKfXcdMq3ckd5-28">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-19" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="pilih = 1 ?" vertex="1">
          <mxGeometry height="145" width="380" x="2490" y="2239.5" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-36" edge="1" parent="1" source="9KKj1zGvKfXcdMq3ckd5-23" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="ent">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="6250" y="2291.5" />
              <mxPoint x="6250" y="4773" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-23" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan daftar film&#xa;(no, nama, kategori, harga)" vertex="1">
          <mxGeometry height="104" width="474" x="3213" y="2239.5" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-28" parent="1" style="rhombus;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="pilih = 5 ?" vertex="1">
          <mxGeometry height="145" width="380" x="2490" y="1990" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-30" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="TIDAK" vertex="1">
          <mxGeometry height="65" width="150" x="2630" y="2160" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-35" edge="1" parent="1" source="9KKj1zGvKfXcdMq3ckd5-33" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" target="lh">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="2660" y="740" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-33" parent="1" style="shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=0;fillColor=#FFFFFF;strokeColor=#202020;fontColor=#101010;fontFamily=Arial;fontSize=20;align=center;verticalAlign=middle;spacing=8;strokeWidth=2;" value="Tampilkan &quot;Logout berhasil&quot;" vertex="1">
          <mxGeometry height="85" width="474" x="2460" y="1760" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-34" edge="1" parent="1" source="9KKj1zGvKfXcdMq3ckd5-28" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.463;entryY=0.945;entryDx=0;entryDy=0;entryPerimeter=0;" target="9KKj1zGvKfXcdMq3ckd5-33">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="9KKj1zGvKfXcdMq3ckd5-37" parent="1" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;rounded=0;" value="YA" vertex="1">
          <mxGeometry height="145" width="90" x="3020" y="2230" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>


[flowchart.drawio](https://github.com/user-attachments/files/33101555/flowchart.drawio)



## Penjelasan Alur Flowchart

1.  Program dimulai.
2.  Pengguna melakukan login dengan memasukkan username dan password.
3.  Sistem melakukan pengecekan akun.
4.  Jika login gagal, pengguna diberikan kesempatan mencoba kembali.
5.  Jika login berhasil, sistem membaca role pengguna.
6.  Jika pengguna merupakan admin, maka tersedia menu:
    -   Lihat film
    -   Tambah film
    -   Ubah film
    -   Hapus film
7.  Jika pengguna merupakan user, maka hanya tersedia:
    -   Lihat film
8.  Pengguna dapat memilih logout untuk kembali ke halaman login.
9.  Program selesai ketika pengguna keluar.

------------------------------------------------------------------------

# 3. Dokumentasi Program dan Output

## A. Tampilan Login Admin

![Login Admin](assets/output_login_admin.png)

Penjelasan:

Pada tampilan ini pengguna melakukan login menggunakan akun admin.

Admin memiliki akses penuh terhadap sistem sehingga setelah login
berhasil akan muncul menu pengelolaan film.

------------------------------------------------------------------------

## B. Tampilan Login User

![Login User](assets/output_login_user.png)

Penjelasan:

Pada login user, sistem mengenali role sebagai pengguna biasa.

User hanya mendapatkan akses untuk melihat daftar film dan logout.

------------------------------------------------------------------------

## C. Menu Admin

![Menu Admin](assets/output_menu_admin.png)

Penjelasan:

Menu admin memiliki lima pilihan:

1.  Lihat Film
2.  Tambah Film
3.  Ubah Film
4.  Hapus Film
5.  Logout

Menu tambahan hanya muncul karena akun yang digunakan memiliki role
admin.

------------------------------------------------------------------------

## D. Menu User

![Menu User](assets/output_login_user.png)

Penjelasan:

Menu user lebih terbatas karena hanya dapat melihat film dan melakukan
logout.

Hal ini menunjukkan penerapan sistem hak akses berdasarkan role.

------------------------------------------------------------------------

## E. Menampilkan Daftar Film

![Daftar Film](assets/output_lihat_film.png)

Penjelasan:

Ketika memilih menu lihat film, program menampilkan seluruh data film
yang tersimpan.

Data yang ditampilkan:

-   Nomor film
-   Nama film
-   Kategori
-   Harga tiket

Contoh output:

    1. The Batman | Action | Rp40000
    2. Spirited Away | Animation | Rp40000
    3. Jujutsu Kaisen | Fantasy | Rp40000

------------------------------------------------------------------------

## F. Menambahkan Film Baru

![Tambah Film](assets/output_tambah_film.png)

Penjelasan:

Admin dapat menambahkan film baru dengan memasukkan:

-   Nama film
-   Kategori film
-   Harga film

Data baru akan disimpan menggunakan fungsi append() ke dalam list film.

------------------------------------------------------------------------

# 4. Dokumentasi Penerapan Nilai Tambah

Program ini memiliki beberapa nilai tambah:

## 1. Sistem Role User dan Admin

Program tidak hanya memiliki login biasa, tetapi menerapkan pembagian
hak akses.

Admin memiliki fitur CRUD, sedangkan user hanya dapat melihat data.

------------------------------------------------------------------------

## 2. Validasi Login

Program memberikan batas percobaan login sebanyak tiga kali.

Selain itu, username kosong akan langsung menghentikan program.

------------------------------------------------------------------------

## 3. Error Handling

Program menggunakan try-except untuk mencegah program berhenti ketika
pengguna memasukkan data yang tidak sesuai.

Contohnya ketika harga film harus berupa angka.

------------------------------------------------------------------------

## 4. Random Code

Ketika admin berhasil menambahkan film, program menghasilkan kode acak
sebagai informasi tambahan.

------------------------------------------------------------------------

## 5. Tampilan Terminal Lebih Rapi

Program menggunakan fungsi pembersihan terminal agar perpindahan menu
lebih nyaman digunakan.
