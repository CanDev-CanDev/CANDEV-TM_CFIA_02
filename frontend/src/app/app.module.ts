import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { TabsModule } from 'ngx-bootstrap/tabs';

import { DataComponent } from './data/data.component';
import { NewsComponent } from './news/news.component';
import { DetailsComponent } from './details/details.component';
import { RecallComponent } from './recall/recall.component';

@NgModule({
  declarations: [
    AppComponent,
    DataComponent,
    NewsComponent,
    DetailsComponent,
    RecallComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BsDropdownModule.forRoot(),
    TabsModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
