import { Component, OnInit } from '@angular/core';
import {MainService} from '../../services/main.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(public mS:MainService) { }

  content:any =[];
  history = [];
  loading = false;
  files = 0;
  dirs = 0;

  ngOnInit() {
  	console.log('Vishal Pandey')
    this.loading = true;
    let root = {
      'url': this.mS.apiUrl,
      'name': '/'
    }
    this.history.push(root)
    this.cFetch(root, false)
  }

  cFetch(cont, h=true){
    this.loading = true;
    window.scrollTo(0,0)
    if (cont.type == 'file') {
      window.location.href = cont.url
      this.loading = false;
      return
    }
    this.mS.cFetch(cont.url).subscribe((r:any)=>{
      this.content = r.data
      this.files = r.files
      this.dirs = r.dirs
      if (h) {
        this.history.push(cont);
      }
      this.loading = false;
    })
  }

  navigateHistory(cont){
    let x = []
    for (var i = 0; i <= this.history.indexOf(cont); i++) {
      x.push(this.history[i])
    }
    this.history = x
    this.cFetch(cont, false);
  }

  formatBytes(bytes,decimals) {
    if(bytes == 0) return '0 Bytes';
    var k = 1024,
       dm = decimals <= 0 ? 0 : decimals || 2,
       sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
       i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
  }
}
