// JavaScript Document

function showMenu(index)
{
	obj=document.getElementById("menu"+index);
	arr=obj.getElementsByTagName("a");
	var maxL=9;
	for(i=0;i<arr.length;i++)
	{
		if(maxL<arr[i].innerHTML.length)
		{
			maxL=arr[i].innerHTML.length;
		}
	}
	obj.style.width=parseInt(maxL)*12+12+"px";
	
	for(i=0;i<9;i++)
	{
		document.getElementById("menu"+index).style.display="none"	
	}
	obj.style.display="block";
}


function hiddenMenu(index)
{
	obj=document.getElementById("menu"+index);
	obj.style.display="none";
}
