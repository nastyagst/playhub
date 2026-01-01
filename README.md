A web application built with Django for browsing video games. The system features database connecting Games, Developers, and Genres.

Key Features:

User Authentication: Sign up, Login, and Logout functionality.

Dynamic Content: Browse games by genres and view detailed information.

Database Structure: Implements complex relationships (One-to-Many for Developers, Many-to-Many for Genres and User Libraries).

UI: Responsive interface built with Bootstrap.
[PlayHub.drawio](https://github.com/user-attachments/files/24402582/PlayHub.drawio)
<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36" version="29.2.9">
  <diagram name="Сторінка-1" id="o4S5O6NY7aaXLgL8PHsW">
    <mxGraphModel grid="1" page="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-66" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30.102941176470587;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" value="Gamer(AbstractUser)" vertex="1">
          <mxGeometry height="255.10294117647058" width="209" x="20" y="864" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-67" parent="Dnnhk74tvq_ELjgkOWkv-66" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="bio: text" vertex="1">
          <mxGeometry height="30" width="209" y="30.102941176470587" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-68" parent="Dnnhk74tvq_ELjgkOWkv-66" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="avatar: img" vertex="1">
          <mxGeometry height="30" width="209" y="60.10294117647059" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-69" parent="Dnnhk74tvq_ELjgkOWkv-66" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="username: str" vertex="1">
          <mxGeometry height="30" width="209" y="90.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-70" parent="Dnnhk74tvq_ELjgkOWkv-66" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="email: str" vertex="1">
          <mxGeometry height="30" width="209" y="120.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-71" parent="Dnnhk74tvq_ELjgkOWkv-66" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="password: str" vertex="1">
          <mxGeometry height="30" width="209" y="150.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-72" parent="Dnnhk74tvq_ELjgkOWkv-66" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="first_name: str" vertex="1">
          <mxGeometry height="30" width="209" y="180.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-73" parent="Dnnhk74tvq_ELjgkOWkv-66" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="last_name: str" vertex="1">
          <mxGeometry height="30" width="209" y="210.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-74" parent="Dnnhk74tvq_ELjgkOWkv-66" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;" vertex="1">
          <mxGeometry height="15" width="209" y="240.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-75" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=33.44034090909091;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" value="Developer" vertex="1">
          <mxGeometry height="182.4403409090909" width="182" x="246" y="260" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-76" parent="Dnnhk74tvq_ELjgkOWkv-75" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="name: str" vertex="1">
          <mxGeometry height="33" width="182" y="33.44034090909091" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-77" parent="Dnnhk74tvq_ELjgkOWkv-75" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="country: str" vertex="1">
          <mxGeometry height="33" width="182" y="66.4403409090909" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-78" parent="Dnnhk74tvq_ELjgkOWkv-75" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="description: text" vertex="1">
          <mxGeometry height="33" width="182" y="99.4403409090909" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-79" parent="Dnnhk74tvq_ELjgkOWkv-75" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="image: img" vertex="1">
          <mxGeometry height="33" width="182" y="132.4403409090909" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-80" parent="Dnnhk74tvq_ELjgkOWkv-75" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;" vertex="1">
          <mxGeometry height="17" width="182" y="165.4403409090909" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-81" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=44.7875;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" value="Genre" vertex="1">
          <mxGeometry height="111.7875" width="116" x="279" y="936" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-82" parent="Dnnhk74tvq_ELjgkOWkv-81" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="name: str" vertex="1">
          <mxGeometry height="45" width="116" y="44.7875" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-83" parent="Dnnhk74tvq_ELjgkOWkv-81" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;" vertex="1">
          <mxGeometry height="22" width="116" y="89.7875" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-84" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30.102941176470587;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" value="Game" vertex="1">
          <mxGeometry height="255.10294117647058" width="199" x="237" y="526" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-85" parent="Dnnhk74tvq_ELjgkOWkv-84" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="title: str" vertex="1">
          <mxGeometry height="30" width="199" y="30.102941176470587" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-86" parent="Dnnhk74tvq_ELjgkOWkv-84" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="description: text" vertex="1">
          <mxGeometry height="30" width="199" y="60.10294117647059" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-87" parent="Dnnhk74tvq_ELjgkOWkv-84" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="release_date: date" vertex="1">
          <mxGeometry height="30" width="199" y="90.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-88" parent="Dnnhk74tvq_ELjgkOWkv-84" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="image: img" vertex="1">
          <mxGeometry height="30" width="199" y="120.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-89" parent="Dnnhk74tvq_ELjgkOWkv-84" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="developer: Developer" vertex="1">
          <mxGeometry height="30" width="199" y="150.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-90" parent="Dnnhk74tvq_ELjgkOWkv-84" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="genres: List[Genre]" vertex="1">
          <mxGeometry height="30" width="199" y="180.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-91" parent="Dnnhk74tvq_ELjgkOWkv-84" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="gamers: List[Gamer]" vertex="1">
          <mxGeometry height="30" width="199" y="210.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-92" parent="Dnnhk74tvq_ELjgkOWkv-84" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;" vertex="1">
          <mxGeometry height="15" width="199" y="240.10294117647058" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-93" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=33.44034090909091;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" value="Comment" vertex="1">
          <mxGeometry height="182.4403409090909" width="214" x="176" y="1202" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-94" parent="Dnnhk74tvq_ELjgkOWkv-93" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="text: text" vertex="1">
          <mxGeometry height="33" width="214" y="33.44034090909091" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-95" parent="Dnnhk74tvq_ELjgkOWkv-93" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="created_at: datetime" vertex="1">
          <mxGeometry height="33" width="214" y="66.4403409090909" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-96" parent="Dnnhk74tvq_ELjgkOWkv-93" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="user: Gamer" vertex="1">
          <mxGeometry height="33" width="214" y="99.4403409090909" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-97" parent="Dnnhk74tvq_ELjgkOWkv-93" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;" value="game: Game" vertex="1">
          <mxGeometry height="33" width="214" y="132.4403409090909" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-98" parent="Dnnhk74tvq_ELjgkOWkv-93" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;" vertex="1">
          <mxGeometry height="17" width="214" y="165.4403409090909" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-99" edge="1" parent="1" source="Dnnhk74tvq_ELjgkOWkv-75" style="curved=1;startArrow=diamondThin;startSize=14;startFill=1;endArrow=none;exitX=0.5;exitY=1;entryX=0.5;entryY=0;rounded=0;" target="Dnnhk74tvq_ELjgkOWkv-84" value="created">
          <mxGeometry relative="1" as="geometry">
            <Array as="points" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-100" parent="Dnnhk74tvq_ELjgkOWkv-99" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=right;verticalAlign=top;" value="1" vertex="1">
          <mxGeometry relative="1" x="-1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-101" parent="Dnnhk74tvq_ELjgkOWkv-99" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=left;verticalAlign=bottom;" value="n" vertex="1">
          <mxGeometry relative="1" x="1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-102" edge="1" parent="1" source="Dnnhk74tvq_ELjgkOWkv-84" style="curved=1;startArrow=none;endArrow=open;endSize=12;exitX=0.5;exitY=1;entryX=0.5;entryY=0;rounded=0;" target="Dnnhk74tvq_ELjgkOWkv-81" value="genres">
          <mxGeometry relative="1" as="geometry">
            <Array as="points" />
          </mxGeometry>
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-103" parent="Dnnhk74tvq_ELjgkOWkv-102" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=right;verticalAlign=top;" value="0..n" vertex="1">
          <mxGeometry relative="1" x="-1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-104" parent="Dnnhk74tvq_ELjgkOWkv-102" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=left;verticalAlign=bottom;" value="0..n" vertex="1">
          <mxGeometry relative="1" x="1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-105" edge="1" parent="1" source="Dnnhk74tvq_ELjgkOWkv-84" style="curved=1;startArrow=open;startSize=12;endArrow=open;endSize=12;exitX=0;exitY=0.8;entryX=0.5;entryY=0;rounded=0;" target="Dnnhk74tvq_ELjgkOWkv-66" value="library">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="125" y="827" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-106" parent="Dnnhk74tvq_ELjgkOWkv-105" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=right;verticalAlign=top;" value="0..n" vertex="1">
          <mxGeometry relative="1" x="-1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-107" parent="Dnnhk74tvq_ELjgkOWkv-105" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=left;verticalAlign=bottom;" value="0..n" vertex="1">
          <mxGeometry relative="1" x="1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-108" edge="1" parent="1" source="Dnnhk74tvq_ELjgkOWkv-66" style="curved=1;startArrow=none;endArrow=none;exitX=0.5;exitY=1;entryX=0;entryY=0.03;rounded=0;" target="Dnnhk74tvq_ELjgkOWkv-93" value="writes">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="125" y="1165" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-109" parent="Dnnhk74tvq_ELjgkOWkv-108" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=right;verticalAlign=top;" value="1" vertex="1">
          <mxGeometry relative="1" x="-1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-110" parent="Dnnhk74tvq_ELjgkOWkv-108" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=left;verticalAlign=bottom;" value="n" vertex="1">
          <mxGeometry relative="1" x="1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-111" edge="1" parent="1" source="Dnnhk74tvq_ELjgkOWkv-84" style="curved=1;startArrow=none;endArrow=none;exitX=0.91;exitY=1;entryX=1;entryY=0.03;rounded=0;" target="Dnnhk74tvq_ELjgkOWkv-93" value="has">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="442" y="827" />
              <mxPoint x="442" y="1165" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-112" parent="Dnnhk74tvq_ELjgkOWkv-111" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=right;verticalAlign=top;" value="1" vertex="1">
          <mxGeometry relative="1" x="-1" as="geometry" />
        </mxCell>
        <mxCell id="Dnnhk74tvq_ELjgkOWkv-113" parent="Dnnhk74tvq_ELjgkOWkv-111" style="edgeLabel;resizable=0;labelBackgroundColor=none;fontSize=12;align=left;verticalAlign=bottom;" value="n" vertex="1">
          <mxGeometry relative="1" x="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
